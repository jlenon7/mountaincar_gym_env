from src.env import env
from src.agents import simple_agent

observation = env.reset()[0]

while True:
    env.render()
    action = simple_agent(observation)

    observation, reward, terminated, truncated, info = env.step(action)

    if terminated:
        break
