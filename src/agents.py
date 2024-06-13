def simple_agent(observation):
    position, velocity = observation

    # If the car is in the valley or a little
    # to the left or starting to come up the
    # hill, go to the right (action=2).
    if -0.1 < position < 0.4:
        return 2

    # If the car is going to the left hand side hill
    # we can't counteract the momentum going to the
    # right. So instead we will intensify it by going
    # to the left (action=1) until gravity pushes the
    # car down the hill.
    if velocity < 0 and position < -0.2:
        # Go to the left
        return 0

    # If any of the above requirements met, the car will
    # not perform any action. The only thing that will
    # make the car move at this point is the momentum.
    return 1
