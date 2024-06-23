import numpy as np
import src.constants as const

def create_bins(bins_per_obs=10):
  bins_car_position = np.linspace(-1.2, 0.6, bins_per_obs)
  bins_car_velocity = np.linspace(-0.07, 0.07, bins_per_obs)

  return np.array([
      bins_car_position, 
      bins_car_velocity
  ])

def discretize_obs(observations):
  binned_observations = []
  
  for i, observation in enumerate(observations):
    discretized_obs = np.digitize(observation, const.BINS[i])

    binned_observations.append(discretized_obs)

  return tuple(binned_observations)

def action_selection(epsilon, discrete_state):
    random_number = np.random.random()

    # EXPLOITATION (choose the action that maximizes Q)
    if random_number > epsilon:
        state = const.Q_TABLE[discrete_state]

        return np.argmax(state)

    # EXPLORATION (choose random action)
    return np.random.choice([
        const.ACTION.LEFT,
        const.ACTION.STOP,
        const.ACTION.RIGHT
    ])

def compute_next_q_value(reward, old_q_value, next_q_value):
    return old_q_value + const.ALPHA * (reward + const.GAMMA * next_q_value - old_q_value)

def reduce_epsilon(epsilon, epoch):
    if const.BURN_IN <= epoch <= const.EPSILON_END:
      return epsilon - const.EPSILON_REDUCE
    
    return epsilon
