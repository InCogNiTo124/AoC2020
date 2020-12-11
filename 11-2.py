import sys
from copy import deepcopy
import itertools as it

EMPTY = 'L'
OCCUPIED = '#'

def eight_neighbourhood(i, j, limit_down, limit_right):
    return ((x, y) for x, y in it.product(range(i-1, i+2), range(j-1, j+2)) if (x, y) != (i, j) and 0 <= x < limit_down and 0 <= y < limit_right)

def get_occupied_queen(x, i, j, limit_down, limit_right):
    directions = ((a, b) for a, b in it.product(range(-1, 2), range(-1, 2)) if a**2 + b**2 > 0)
    occupied = 0
    for dir_i, dir_j in directions:
        start_i = i
        start_j = j
        while True:
            start_i += dir_i
            start_j += dir_j
            if not (0 <= start_i < limit_down) or not (0 <= start_j < limit_right):
                break
            if x[start_i][start_j] == OCCUPIED:
                occupied += 1
                break
            if x[start_i][start_j] == EMPTY:
                break
    return occupied

def transform(x):
    y = deepcopy(x)
    for i in range(len(x)):
        line = x[i]
        for j in range(len(line)):
            seat = x[i][j]
            #occupied = sum(1 for a, b in eight_neighbourhood(i, j, len(x), len(line)) if x[a][b] == OCCUPIED)
            occupied = get_occupied_queen(x, i, j, len(x), len(line))
            if seat == EMPTY and occupied == 0:
                y[i][j] = OCCUPIED
            elif seat == OCCUPIED and occupied >= 5:
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

