import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import gym
import matplotlib.pyplot as plt
import pickle

# Hyper Parameters
BATCH_SIZE = 1000
LR = 2e-3  # learning rate
EPSILON = 0.9  # greedy policy
GAMMA = 0.9  # reward discount
TARGET_REPLACE_ITER = 100  # target update frequency
MEMORY_CAPACITY = 30000
env = gym.make('Guesswho-v0')
env = env.unwrapped
env.game.setAgentType('optimal')

N_ACTIONS = env.action_space.n
N_STATES = env.observation_space.shape[0]
ENV_A_SHAPE = 0 if isinstance(env.action_space.sample(),
                              int) else env.action_space.sample().shape  # to confirm the shape
FILENAME = 'DQN'


class Net(nn.Module):
    def __init__(self, ):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(N_STATES, 512)
        self.fc1.weight.data.normal_(0, 0.1)  # initialization
        self.out = nn.Linear(512, N_ACTIONS)
        self.out.weight.data.normal_(0, 0.1)  # initialization

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        actions_value = self.out(x)
        return actions_value


class DQN(object):
    def __init__(self):
        self.eval_net, self.target_net = Net(), Net()

        self.learn_step_counter = 0  # for target updating
        self.memory_counter = 0  # for storing memory
        self.memory = np.zeros((MEMORY_CAPACITY, N_STATES * 2 + 2))  # initialize memory
        self.optimizer = torch.optim.Adam(self.eval_net.parameters(), lr=LR)
        self.loss_func = nn.MSELoss()

    def choose_action(self, x):
        x = torch.unsqueeze(torch.FloatTensor(x), 0)
        # input only one sample
        if np.random.uniform() < EPSILON:  # greedy
            actions_value = self.eval_net.forward(x)
            action = torch.max(actions_value, 1)[1].data.numpy()
            action = action[0] if ENV_A_SHAPE == 0 else action.reshape(ENV_A_SHAPE)  # return the argmax index
        else:  # random
            action = np.random.randint(0, N_ACTIONS)
            action = action if ENV_A_SHAPE == 0 else action.reshape(ENV_A_SHAPE)
        return action

    def store_transition(self, s, a, r, s_):
        transition = np.hstack((s, [a, r], s_))
        # replace the old memory with new memory
        index = self.memory_counter % MEMORY_CAPACITY
        self.memory[index, :] = transition
        self.memory_counter += 1

    def learn(self):
        # target parameter update
        if self.learn_step_counter % TARGET_REPLACE_ITER == 0:
            self.target_net.load_state_dict(self.eval_net.state_dict())
        self.learn_step_counter += 1

        # sample batch transitions
        sample_index = np.random.choice(MEMORY_CAPACITY, BATCH_SIZE)
        b_memory = self.memory[sample_index, :]
        b_s = torch.FloatTensor(b_memory[:, :N_STATES])
        b_a = torch.LongTensor(b_memory[:, N_STATES:N_STATES + 1].astype(int))
        b_r = torch.FloatTensor(b_memory[:, N_STATES + 1:N_STATES + 2])
        b_s_ = torch.FloatTensor(b_memory[:, -N_STATES:])

        # q_eval w.r.t the action in experience
        q_eval = self.eval_net(b_s).gather(1, b_a)  # shape (batch, 1)
        q_next = self.target_net(b_s_).detach()  # detach from graph, don't backpropagate
        q_target = b_r + GAMMA * q_next.max(1)[0].view(BATCH_SIZE, 1)  # shape (batch, 1)
        loss = self.loss_func(q_eval, q_target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


def saveDQN(deeQueEnn):
    menuKey = int(input("Save Neural Network?\n1) Yes\n2) No\nInput: "))
    if menuKey == 1:
        savedName = str(input("Filename to save as (enter -1 for default): "))
        if savedName == "-1":
            outfile = open(FILENAME, 'wb')

            pickle.dump(deeQueEnn, outfile)
            outfile.close()
        else:
            outfile = open(savedName, 'wb')

            pickle.dump(deeQueEnn, outfile)
            outfile.close()


def loadDQN():
    menuKey = int(input("Load Neural Network?\n1) Yes\n2) No\nInput: "))
    if menuKey == 1:
        loadName = str(input("Filename to load (enter -1 for default): "))
        if loadName == "-1":
            infile = open(FILENAME, 'rb')

            deeQueEnn = pickle.load(infile)
            infile.close()
        else:
            try:
                infile = open(loadName, 'rb')
            except IOError:
                print("File not found, opening default file.\n")
                infile = open(FILENAME, 'rb')
            deeQueEnn = pickle.load(infile)
            infile.close()

    else:
        deeQueEnn = DQN()

    return deeQueEnn

def simulate(i):
    x_axis = []
    wins = 0
    y_axis = []

    #saveCSV = open("QNNData.csv", 'w')

    for i_episode in range(i):
        s = env.reset()
        ep_r = 0
        while True:
            print(s)
            a = dqn.choose_action(s)

            # take action
            s_, r, done, info = env.step(a)

            dqn.store_transition(s, a, r, s_)

            ep_r += r
            if dqn.memory_counter > MEMORY_CAPACITY:
                dqn.learn()

            if env.status == 'WON':
                wins += 1

            if done:
                break

            s = s_

        if i_episode != 0:
            y_axis.append((wins / i_episode) * 100)
            x_axis.append(i_episode)

            #saveCSV.write(str(str(wins) + ","))
            #saveCSV.write(str(str(i_ep) + "\n"))

    #saveCSV.close()
    return x_axis, y_axis


dqn = loadDQN()

for j in range(1, 6):
    x_axis, y_axis = simulate(10000)
    l = "Run #" + str(j)
    plt.plot(x_axis, y_axis, label=l)

saveDQN(dqn)

plt.legend()
plt.xlim(0, 10000)
plt.ylim(0, 100)
plt.tight_layout()

plt.ylabel('Wins (%)')
plt.xlabel('Number of Episodes')
plt.show()
