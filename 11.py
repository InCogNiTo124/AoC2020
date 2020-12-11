import sys
from copy import deepcopy
import itertools as it

EMPTY = 'L'
OCCUPIED = '#'

def eight_neighbourhood(i, j, limit_down, limit_right):
    return ((x, y) for x, y in it.product(range(i-1, i+2), range(j-1, j+2)) if (x, y) != (i, j) and 0 <= x < limit_down and 0 <= y < limit_right)

def transform(x):
    y = deepcopy(x)
    for i in range(len(x)):
        line = x[i]
        for j in range(len(line)):
            seat = x[i][j]
            occupied = sum(1 for a, b in eight_neighbourhood(i, j, len(x), len(line)) if x[a][b] == OCCUPIED)
            if seat == EMPTY and occupied == 0:
                y[i][j] = OCCUPIED
            elif seat == OCCUPIED and occupied >= 4:
                y[i][j] = EMPTY
    return y

ferry = [list(line.strip()) for line in sys.stdin]
while True:
    ferry2 = transform(ferry)
    if ferry2 == ferry:
        print(sum(1 for t in ferry for x in t if x == OCCUPIED))
        break
    else:
        ferry = ferry2

