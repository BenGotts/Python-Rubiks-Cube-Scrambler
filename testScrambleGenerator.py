import random

moves = ["U", "D", "F", "B", "R", "L"]
dir = ["", "'", "2"]
slen = random.randint(25, 28)

def gen_scramble():
    s = valid([[random.choice(moves), random.choice(dir)] for x in range(slen)])
    return ''.join(str(s[x][0]) + str(s[x][1]) + ' ' for x in range(len(s))) + '[' + str(slen) + ']'

def valid(ar):
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    return ar


s = gen_scramble()
print(s)
