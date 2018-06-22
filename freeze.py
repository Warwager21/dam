# Load the framework
import gym
import scipy
#Load the environment
env = gym.make('FrozenLake-v0')
print(env.observation_space)
print(env.action_space)

score = 0
#for a bunch of episodes
for _ in range(10000):
    #refresh and render the initial state
    env.reset()
    for t in range(100):  #take 100 steps
        #through trial, we know that
        # 0 = LEFT
        # 1 = DOWN
        # 2 = RIGHT
        # 3 = UP
        # and [env.action_space.sample()] = random move
        obs, rew, done, info = env.step(env.action_space.sample())
        if done:
           score += rew
           break
print(score)