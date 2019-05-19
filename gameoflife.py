import pprint

def dead_state(w,h):
    return [[0 for i in range(w)] for j in range(h)]

pprint.pprint(dead_state(5,5))
    
