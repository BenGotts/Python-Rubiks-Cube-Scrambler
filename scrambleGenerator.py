import random
import sys
from scrambleImage import scramble

moves = ["U", "D", "F", "B", "R", "L"]
dir = ["", "'", "2"]
slen = random.randint(25, 28)

def gen_scramble():
    # Make array of arrays that represent moves ex. U' = ['U', "'"]
    s = valid([[random.choice(moves), random.choice(dir)] for x in range(slen)])
    cube = scramble(s, slen)

    # Format scramble to a string with movecount
    return ''.join(str(s[x][0]) + str(s[x][1]) + ' ' for x in range(len(s))) + "[" + str(slen) + "]"

def valid(ar):
    # Check if Move behind or 2 behind is the same as the random move
    # this gets rid of 'R R2' or 'R L R2' or similar for all moves
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    for x in range(2, len(ar)):
        while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    return ar
 
s = gen_scramble()
print(s)
