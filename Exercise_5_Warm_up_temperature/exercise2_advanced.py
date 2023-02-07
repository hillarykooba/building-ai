import random
import numpy as np

def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing

    return clamp(np.exp(-(S_old - S_new)/T), 0.0, 1.0)

# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

accept(150, 140, 15)
