import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding
import os, subprocess, time, signal
from gym.envs.guesswho.game import Game

class GuesswhoEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(37) #the 37 actions 
        low = np.zeros(2, dtype=int)
        high = np.array((24, 24), dtype=int)
        self.observation_space = spaces.Box(low, high)
        self.status = 'START' #inital status 
        self.game = Game() #game object 

    def _step(self, action):
        self._take_action(action)  #take action in game
        self.status = self.game.step()  #update status
        reward = self._get_reward()  #reward from action
        ob = self.game.getState()  #state observation 
        episode_over = (self.status == 'LOST' or self.status == 'WON')
        print("OVER? " + str(episode_over)) #end episode if game over 
        return ob, reward, episode_over, {} #the {} is a dictionary that can contain debug info 

    def _seed(self, seed):
        np.random.seed

    def _reset(self):
        self.status = 'START'
        self.game.resetBoard()
        print(self.game.getState())
        return self.game.getState()

    def _render(self, mode='human', close=False):
        pass

    def _take_action(self, action):
        self.game.oneTurn(action)

    def _get_reward(self):
        #Reward given for flipping tiles or winning
        if self.status == 'WON':
            return 50
        elif self.status == 'LOST' or self.status == 'START':
            return 0
        else:
            return int(self.status)