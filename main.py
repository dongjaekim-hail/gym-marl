import gymnasium as gym
from time import sleep
env = gym.make('MiniGrid-Empty-5x5-v0',render_mode='human')

observation, info = env.reset()
for _ in range(1000):
   action = env.action_space.sample()  # User-defined policy function
   observation, reward, terminated, truncated, info = env.step(action)
   env.render()
   sleep(0.2)
   if terminated or truncated:
      observation, info = env.reset()
env.close()
# env.render()