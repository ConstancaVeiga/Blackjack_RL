# Sensitivity analysis of algorithm
import matplotlib.pyplot as plt

def train_agent(alpha, episodes):
  agent_qv = BlackjackQVLearning(alpha=alpha)
  agent_qv.train(episodes)

  return agent_qv

def test_agent(model, test_games):
  # test_games = 100000
  wins_qv = 0
  losses_qv = 0
  draws_qv = 0

  one_percent = round(test_games / 100)

  for idx in range(test_games):

      if idx % one_percent == 0:
          progress = (idx / test_games) * 100
          print(f"Testing progress: {progress:.2f}%")
      result = agent_qv.play()
      # print(result)
      if result == "win":
          wins_qv += 1
      elif result == "loss":
          losses_qv += 1
      else:
          draws_qv += 1

  return wins_qv, losses_qv, draws_qv

def average_list(list):
  return sum(list)/len(list)

# SENSITIVITY ANALYSIS OF VARYING ALPHA AND KEEPING CONSTANT GAMMA
alpha = np.arange(0.05, 0.16, 0.01)
gamma = 0.89

iterations = 3

win_rate = []

for a in alpha:
  print('Testing alpha = ', a)
  win_rate_tmp = []

  for idx in range(iterations):
    print(f'Iteration {idx} of alpha = {a}')
    np.random.seed(idx)

    agent_qv = train_agent(alpha=a, episodes=5000000)

    print("Running agent testing")

    wins_qv, losses_qv, draws_qv = test_agent(model=agent_qv, test_games=100000)

    print(f"Wins: {wins_qv}, Losses: {losses_qv}, Draws: {draws_qv}")
    print(f"Win rate: {wins_qv/(wins_qv + losses_qv)*100:.2f}%")

    win_rate_tmp.append(wins_qv/(wins_qv + losses_qv)*100)

  win_rate.append(average_list(win_rate_tmp))

  print(' ')

print(f'Alpha: {alpha}')
print(f'win_rates: {win_rate}')


######################################################################################################################################################################################################################################################################

# the following alphas and corresponding win rates were extracted after a run 
alpha = [0.05, 0.06, 0.07, 0.08, 0.09, 0.1,  0.11, 0.12, 0.13, 0.14, 0.15]
win_rates = [41.678581646377395, 41.50972132992829, 41.956392657540455, 41.93974737616626, 40.813534477503524, 40.021653553031115, 41.35608255303342, 42.06754118633868, 40.34377364003922, 40.795772608361055, 40.748505654651886]

plt.plot(alpha, win_rates, marker=".")
plt.grid()
plt.xlabel(r'$\alpha$')
plt.ylabel('Win rate (%)')
plt.show()

######################################################################################################################################################################################################################################################################

def train_agent(alpha, gamma, episodes):
  agent_qv = BlackjackQVLearning(alpha=alpha, gamma=gamma)
  agent_qv.train(episodes)

  return agent_qv

# SENSITIVITY ANALYSIS OF VARYING GAMMA AND KEEPING CONSTANT ALPHA OF 0.12
alpha = 0.12 #np.arange(0.05, 0.16, 0.01)
gamma = np.arange(0.88, 0.99, 0.01)

iterations = 3

win_rate = []

for g in gamma:
  print('Testing gamma = ', g)
  win_rate_tmp = []

  for idx in range(iterations):
    print(f'Iteration {idx} of gamma = {g}')
    np.random.seed(idx)

    agent_qv = train_agent(alpha=alpha, gamma=g, episodes=5000000)

    print("Running agent testing")

    wins_qv, losses_qv, draws_qv = test_agent(model=agent_qv, test_games=100000)

    print(f"Wins: {wins_qv}, Losses: {losses_qv}, Draws: {draws_qv}")
    print(f"Win rate: {wins_qv/(wins_qv + losses_qv)*100:.2f}%")

    win_rate_tmp.append(wins_qv/(wins_qv + losses_qv)*100)

  win_rate.append(average_list(win_rate_tmp))

  print(' ')

print(f'Gamma: {gamma}')
print(f'win_rates: {win_rate}')

######################################################################################################################################################################################################################################################################

# the following gammas and corresponding win rates were extracted after a run 
gamma =  [0.88, 0.89, 0.9,  0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98]
win_rates = [40.963345480457434, 41.82035974449786, 41.330546762082605, 41.492530276404096, 40.54576571269862, 41.03874335320247, 41.23203826325365, 41.06479636034001, 40.62343054416035, 41.59060211134196, 40.99807231798071]
plt.plot(gamma, win_rates, marker=".")
plt.grid()
plt.xlabel(r'$\gamma$')
plt.ylabel('Win rate (%)')
plt.show()

######################################################################################################################################################################################################################################################################

