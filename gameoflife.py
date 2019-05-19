import pprint
import random


def dead_state(width,height):
    return [[0 for i in range(width)] for j in range(height)]
# pprint.pprint(dead_state(5,5))
def state_width(state):
    return len(state)

def state_height(state):
    return len(state[0])



def random_state(width,height):
    state = dead_state(width,height)

    for i in range(0,state_width(state)):
        for y in range (0,state_height(state)):
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
    for y in range(state_height(state)):
        #state here is 20
        line = '          '
        for x in range(state_width(state)):
          line += display_as[state[x][y]] * 2
        lines.append(line)
    print "\n".join(lines)
  
# a_dead_state = dead_state(10,10)
a_random_state = random_state(20,30)
render(a_random_state)

