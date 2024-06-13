import gym
from src.constants import ENV_NAME


env = gym.make(ENV_NAME,  render_mode='human')
rgb_env = gym.make(ENV_NAME, render_mode='rgb_array')
