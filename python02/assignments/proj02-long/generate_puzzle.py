#! /usr/bin/python3

import sys
import random
import string



words = []
for line in sys.stdin:
    words.append(line.strip())

print(words)

longest_word = max( len(s) for s in words )
wid = longest_word * random.randint(15,20) // 10
hei = longest_word * random.randint(15,20) // 10


grid = []
for i in range(wid):
    grid.append( [' ']*hei )


DIRS = [(1,0), (0,1), (-1,0), (0,-1),
        (1,1), (-1,1), (1,-1), (-1,-1)]

for w in words:
    if random.randint(0,10) > 7:
        print(f"Skipping '{w}'")
        continue   # skip this word entirely

    print(f"Generating '{w}' ", end='')

    tries = 1000
    while tries > 0:
        if tries % 50 == 1:
            print(".", end='')

        start_x = random.randint(0,wid-1)
        start_y = random.randint(0,hei-1)

        dir = DIRS[random.randint(0,7)]

        if start_x + len(w)*dir[0] >= wid or \
           start_x + len(w)*dir[0] <  0   or \
           start_y + len(w)*dir[1] >= hei or \
           start_y + len(w)*dir[1] <  0:
            tries -= 1
            continue

        ok = True
        for i in range(len(w)):
            x = start_x + i*dir[0]
            y = start_y + i*dir[1]
            if grid[x][y] not in ' '+w[i]:
                ok = False
                break

        if not ok:
            tries -= 1
            continue

        # install the word!
        for i in range(len(w)):
            x = start_x + i*dir[0]
            y = start_y + i*dir[1]
            grid[x][y] = w[i]
        break

    if tries == 0:
        print("FAIL")
    else:
        print(f"OK, with {tries} tries remaining")

print()
print()
print()



for y in range(hei):
    for x in range(wid):
        if grid[x][y] == ' ':
            print(string.ascii_lowercase[random.randint(0,25)], end='')
        else:
            print(grid[x][y], end='')
    print()


print()   # the blank line

for w in words:
    print(w)


