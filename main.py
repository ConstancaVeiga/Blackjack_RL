from environment import BlackjackENV
from environment_withSplit import BlackjackENVsplit
from QV_learning import

# Train the agent
agent_q = BlackjackQLearning()
episodes = 5000000  # Number of training episodes
agent_q.train(episodes)

# Test the agent's performance
test_games = 100000
wins_q = 0
losses_q = 0
draws_q = 0

for _ in range(test_games):
    print("-----")
    result = agent_q.play()
    print(result)
    if result == "win":
        wins_q += 1
    elif result == "loss":
        losses_q += 1
    else:
        draws_q += 1

print(f"Number of Wins: {wins_q}")
print(f"Number of Losses: {losses_q}")
print(f"Number of Draws: {draws_q}")
print(f"Win rate is: {wins_q/(wins_q + losses_q)*100:.2f}%")

