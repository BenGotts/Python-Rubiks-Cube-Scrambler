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

scramble(s, slen)

# scramble([["R", ""], ["U", ""], ["R", "'"]], 1)

scr = ""
for x in range(len(s)):
    scr += str(s[x][0]) + str(s[x][1]) + " "
scr += "[" + str(slen) + "]"

image(scr)
