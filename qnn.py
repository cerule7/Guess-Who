import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import gym
import matplotlib.pyplot as plt
import pickle
import _thread as thread

# Hyper Parameters
BATCH_SIZE = 32
LR = 0.91 # learning rate
EPSILON = 0.9               # greedy policy
GAMMA = 0.9                 # reward discount
TARGET_REPLACE_ITER = 100   # target update frequency
MEMORY_CAPACITY = 2000
env = gym.make('Guesswho-v0')
env = env.unwrapped
env.game.setAgentType('none')
N_ACTIONS = env.action_space.n
N_STATES = env.observation_space.shape[0]
ENV_A_SHAPE = 0 if isinstance(env.action_space.sample(), int) else env.action_space.sample().shape     # to confirm the shape
FILENAME = 'DQN'


class Net(nn.Module):
    def __init__(self, ):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(N_STATES, 50)
        self.fc1.weight.data.normal_(0, 0.1)   # initialization
        self.out = nn.Linear(50, N_ACTIONS)
        self.out.weight.data.normal_(0, 0.1)   # initialization

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        actions_value = self.out(x)
        return actions_value


class DQN(object):
    def __init__(self):
        self.eval_net, self.target_net = Net(), Net()

        self.learn_step_counter = 0                                     # for target updating
        self.memory_counter = 0                                         # for storing memory
        self.memory = np.zeros((MEMORY_CAPACITY, N_STATES * 2 + 2))     # initialize memory
        self.optimizer = torch.optim.Adam(self.eval_net.parameters(), lr=LR)
        self.loss_func = nn.MSELoss()

    def choose_action(self, x):
        x = torch.unsqueeze(torch.FloatTensor(x), 0)
        # input only one sample
        if np.random.uniform() < EPSILON:   # greedy
            actions_value = self.eval_net.forward(x)
            action = torch.max(actions_value, 1)[1].data.numpy()
            action = action[0] if ENV_A_SHAPE == 0 else action.reshape(ENV_A_SHAPE)  # return the argmax index
        else:   # random
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
        b_a = torch.LongTensor(b_memory[:, N_STATES:N_STATES+1].astype(int))
        b_r = torch.FloatTensor(b_memory[:, N_STATES+1:N_STATES+2])
        b_s_ = torch.FloatTensor(b_memory[:, -N_STATES:])

        # q_eval w.r.t the action in experience
        q_eval = self.eval_net(b_s).gather(1, b_a)  # shape (batch, 1)
        q_next = self.target_net(b_s_).detach()     # detach from graph, don't backpropagate
        q_target = b_r + GAMMA * q_next.max(1)[0].view(BATCH_SIZE, 1)   # shape (batch, 1)
        loss = self.loss_func(q_eval, q_target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
def saveDQN(deeQueEnn):
        
        outfile = open(FILENAME, 'wb')
        
        pickle.dump(deeQueEnn, outfile)
        outfile.close()
        
def loadDQN():
        
        infile = open(FILENAME, 'rb')
        
        deeQueEnn = pickle.load(infile)
        infile.close()
        
        return deeQueEnn

status = ['up', 'down']
risk = ['safe', 'risky']
actions = np.array([[0, 0], [0, 0]])

def simulate(i):
    x_axis = []
    wins = 0
    y_axis = []
    for i_episode in range(i):
        s = env.reset()
        ep_r = 0
        while True:
            a = dqn.choose_action(s)

            if(s[20] == 1):
                if(a != 13):
                    actions[1,0] += 1
                else:
                    actions[0,0] += 1
            else:
                if(a != 13):
                    actions[1,1] += 1
                else:
                    actions[0,1] += 1

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

    return x_axis, y_axis

keyIn = int(input("Load Neural Network?\n1) Yes\n2) No\nInput: "))
if keyIn == 1:
    dqn = loadDQN()
else:
    dqn = DQN()

p, k = simulate(10000)

for j in range(1, 11):
    x_axis, y_axis = simulate(5000)
    l = "number = " + str(j)
    plt.plot(x_axis, y_axis,label=l)

# fig, ax = plt.subplots()
# im = ax.imshow(actions)
# ax.set_xticks(np.arange(len(status)))
# ax.set_yticks(np.arange(len(risk)))
# ax.set_xticklabels(status)
# ax.set_yticklabels(risk)
# plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
# for i in range(len(risk)):
#     for j in range(len(status)):
#         text = ax.text(j, i, actions[i, j], ha="center", va="center", color="w")
# ax.set_title("Distribution of Actions")
# fig.tight_layout()
# plt.show()

thread.start_new_thread(saveDQN, (dqn,))

plt.legend()
plt.ylabel('Win-loss ratio (%)')
plt.xlabel('Number of Episodes')
plt.show()