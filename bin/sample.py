from src.env import env

env.reset()

while True:
    # 0 right
    # 1 stop
    # 2 left
    action = env.action_space.sample()

    env.render()

    observation, reward, terminated, truncated, info = env.step(action)

    print(f"Reward: {reward}")
    print(f"Terminated: {terminated}")
    print(f"Truncated: {truncated}")
    print(f"Info: {info}")

    if terminated:
        break
