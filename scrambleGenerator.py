import random
from scrambleImage import scramble
from scrambleImage import image

moves = ["U", "D", "F", "B", "R", "L"]
dir = ["", "'", "2"]
slen = random.randint(25, 28)

def scramble_gen():
    scramble = [0] * slen
    for x in range(len(scramble)):
        scramble[x] = [0] * 2
    return scramble

def scramble_replace(ar):
    for x in range(len(ar)):
        ar[x][0] = random.choice(moves)
        ar[x][1] = random.choice(dir)
    return ar

def valid(ar):
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    for x in range(2, len(ar)):
        while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    return ar

def sprint(ar):
    for x in range(len(ar)):
        print(str(ar[x][0]) + str(ar[x][1]), end = " ")

s = scramble_replace(scramble_gen())
valid(s)
# sprint(valid(s))
# print("[" + str(slen) + "]\n")

cube = scramble(s, slen)

scr = ""
for x in range(len(s)):
    scr += str(s[x][0]) + str(s[x][1]) + " "
scr += "[" + str(slen) + "]"

# with open('test.txt', 'a') as f:
#     f.write(scr + '\n')

image(scr)

for y in range(6):
    for z in range(8):
        if(cube[y][z] == (255,255,255)):
            cube[y][z] = 'w'
        elif(cube[y][z] == (0,165,255)):
            cube[y][z] = 'o'
        elif(cube[y][z] == (0,255,0)):
            cube[y][z] = 'g'
        elif(cube[y][z] == (0,0,255)):
            cube[y][z] = 'r'
        elif(cube[y][z] == (255,0,0)):
            cube[y][z] = 'b'
        elif(cube[y][z] == (0,255,255)):
            cube[y][z] = 'y'

import json

with open('data.json', 'w') as f:
    # f.write(scr + '\n')
    # f.write(str(cube))
    # f.write('\n')
    data = dict([('scramble', scr), ('image', cube)])

    # json.dumps(data)
    json.dump(data, f, indent=2)
