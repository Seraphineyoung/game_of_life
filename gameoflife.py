import pprint
import random

def dead_state(width,height):
    return [0 for i in range(width) for j in range(height)]

# pprint.pprint(dead_state(5,5))

def random_state(width,height):
    randnum = []
    state = dead_state(width,height)
    for i in state:
        rand_num = random.random()
        if rand_num >= 0.5:
            randnum.append(0)
        else:
            randnum.append(1)
    return randnum




pprint.pprint(random_state(5,5))  

