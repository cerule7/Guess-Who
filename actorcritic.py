import torch
import torch.nn as nn
from torch.distributions import Categorical
import torch.optim as optim
import gym
import matplotlib.pyplot as plt
import pickle
import numpy as np

# Hyper Parameters
lr = 1
hidden_size = 256
device = torch.device("cpu")
env = gym.make('Guesswho-v0')
env = env.unwrapped
env.game.setAgentType('optimal')

N_ACTIONS = env.action_space.n
N_STATES = env.observation_space.shape[0]

FILENAME = 'AC'

saveCSV = open("ACData.csv", 'w')
totWins = 0
totEps = 0


class A3C(nn.Module):
    def __init__(self, std=0.0):
        super(A3C, self).__init__()

        self.critic = nn.Sequential(
            nn.Linear(N_STATES, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 1)
        )

        self.actor = nn.Sequential(
            nn.Linear(N_STATES, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, N_ACTIONS),
            nn.Softmax(-1),
        )


    def forward(self, x):
        value = self.critic(x)
        probs = self.actor(x)
        dist = Categorical(probs)
        return dist, value


def test_env():
    state = env.reset()
    done = False
    total_reward = 0
    while not done:
        state = torch.FloatTensor(state).unsqueeze(0).to(device)
        dist, _ = model(state)
        next_state, reward, done, _ = env.step(dist.sample().cpu().numpy()[0])
        state = next_state
        total_reward += reward
    return total_reward


def compute_returns(next_value, rewards, masks, gamma=0.99):
    R = next_value
    returns = []
    for step in reversed(range(len(rewards))):
        R = rewards[step] + gamma * R * masks[step]
        returns.insert(0, R)
    return returns


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
        deeQueEnn = A3C()

    return deeQueEnn

# status = ['up', 'down']
# risk = ['safe', 'risky']
# actions = np.array([[0, 0], [0, 0]])

def simulate(i):
    x_axis = []
    y_axis = []
    wins = 0

    # global totWins
    # global totEps

    for i_ep in range(i):
        state = env.reset()
        while True:

            log_probs = []
            values = []
            rewards = []
            masks = []
            entropy = 0

            for _ in range(0, 1):

                if env.status == 'WON' or env.status == 'LOST':
                    break

                state = torch.FloatTensor(state).to(device)
                dist, value = model(state)

                action = dist.sample()

                next_state, reward, done, _ = env.step(action.cpu().numpy())

                # if(s[20] == 1):
                #     if(env.getNumFlipped() >= int(s[18] / 2) or action != 13):
                #         actions[1,0] += 1
                #     else:
                #         actions[0,0] += 1
                # elif(s[20] == -1):
                #     if(env.getNumFlipped() >= int(s[18] / 2) or action != 13):
                #         actions[1,1] += 1
                #     else:
                #         actions[0,1] += 1

                log_prob = dist.log_prob(action)
                entropy += dist.entropy().mean()

                log_probs.append(log_prob.view(1))
                values.append(value)
                rewards.append(torch.tensor(reward, dtype=torch.float).to(device))
                masks.append(torch.tensor(1 - done, dtype=torch.float).to(device))

                state = next_state

            print(env.status)

            if env.status == 'WON':
                wins += 1
                # totWins += 1
                break
            elif env.status == 'LOST' or env.getNumTurns() > 30:  # time out
                break
            else:
                next_state = torch.FloatTensor(next_state).to(device)
                _, next_value = model(next_state)
                returns = compute_returns(next_value, rewards, masks)

                log_probs = torch.cat(log_probs)
                returns = torch.cat(returns).detach()
                values = torch.cat(values)

                advantage = returns - values

                actor_loss = -(log_probs * advantage.detach()).mean()
                critic_loss = advantage.pow(2).mean()

                loss = actor_loss + 0.5 * critic_loss - 0.001 * entropy

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

        if i_ep is not 0:
            y_axis.append((wins / i_ep) * 100)
            x_axis.append(i_ep)

        # saveCSV.write(str(str(totWins) + ","))
        # saveCSV.write(str(str(totEps) + "\n"))
        #totEps += 1

    return x_axis, y_axis





# simulate(10000)

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

for j in range(1, 6):
    model = A3C()
    optimizer = optim.Adam(model.parameters())
    x_axis, y_axis = simulate(50000)
    l = "Run #" + str(j)
    plt.plot(x_axis, y_axis, label=l)

plt.legend()
plt.xlim(0, 50000)
plt.ylim(0, 100)
plt.tight_layout()

plt.ylabel('Win (%)')
plt.xlabel('Number of Episodes')
plt.show()

saveDQN(model)

# saveCSV.close()