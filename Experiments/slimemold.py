"""
Slime Mold - Cellular Automata Experiment *Draft*
--------
TBD
"""

import numpy as np

eat_rate = 2

food = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0,15,30,10, 0, 0, 0, 0],
    [0, 0, 0,30,80,30, 0, 0, 0, 0],
    [0, 0, 0, 5,10, 8, 0, 0, 0, 0]
])

slime = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,30, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 3, 0, 0, 0]
])

def main(food, slime):
    #while np.sum(food) != 0:
    #feed
    for slime_idx, slime_cell in np.ndenumerate(slime):
        food_cell = food[slime_idx] 
        if food_cell > 0 and slime_cell > 0:
            resource_obtained = 1
            if food_cell > 1:
                resource_obtained = 2
            food[slime_idx] = food_cell - resource_obtained
            slime[slime_idx] += resource_obtained

    #for slime_idx, slime_cell in np.ndenumerate(slime):
    #    if slime_cell > 0:

    return slime

print(main(food, slime))