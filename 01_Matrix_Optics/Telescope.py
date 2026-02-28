import numpy as np
import matplotlib.pyplot as plt

def propagate(d):
    # new_height = height + d * angle
    # new_angle = angle (unchanged)
    return np.array([[1, d],
                     [0, 1]])

def thin_lens(f):
    # new_height = height (unchanged)
    # new_angle = angle - height/f
    return np.array([[1, 0],
                     [-1/f, 1]])