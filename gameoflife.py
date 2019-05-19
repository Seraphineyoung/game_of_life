import pprint
import random


def dead_state(width,height):
    return [[0 for i in range(width)] for j in range(height)]
# pprint.pprint(dead_state(5,5))

def random_state(width,height):
    state = dead_state(width,height)
    for i in range(width):
        for y in range (height):
            random_num = random.random()
            if random_num > 0.65:
                cell_state = 1
            else:
                cell_state = 0
            state[i][y] = cell_state
    return state


def render(state):
    display_as = {
        0: "#",
        1: u"\u2588"
    }
    lines = []
    
    for y in range(len(state)):
        line = '          '
        for x in range(len(state)):
          line += display_as[state[x][y]] * 2
        lines.append(line)
    print "\n".join(lines)

# pprint.pprint(random_state(5,5))  
a_dead_state = dead_state(10,10)
a_random_state = random_state(10,10)
render(a_random_state)

