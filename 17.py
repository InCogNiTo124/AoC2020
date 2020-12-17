import sys
import copy
import pprint
import itertools as it

def generate_neighbours(i, j, k):
    x = range(i-1, i+2)
    y = range(j-1, j+2)
    z = range(k-1, k+2)
    return filter(lambda t: t != (i, j, k), it.product(x, y, z))

INACTIVE = 0
ACTIVE = 1
MAP_SIZE = 30
cube = [[[INACTIVE for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

for i, line in enumerate(sys.stdin):
    bools = list(map(lambda t: int(t=='#'), line.strip()))
    # centering the plane this inputs resides in
    x_plane = MAP_SIZE//2
    y_plane = (MAP_SIZE-len(bools))//2 + i
    z_plane = slice((MAP_SIZE - len(bools))//2, (MAP_SIZE+len(bools))//2)
    cube[x_plane][y_plane][z_plane] = bools

cycles = 6
x_range = range(1, MAP_SIZE-1)
y_range = range(1, MAP_SIZE-1)
z_range = range(1, MAP_SIZE-1)
#pprint.pprint(cube)
for cycle in range(cycles):
    new_cube = copy.deepcopy(cube)
    for (i, j, k) in it.product(x_range, y_range, z_range):
        active_neighbours = sum(cube[a][b][c] for (a, b, c) in generate_neighbours(i, j, k))
        if cube[i][j][k] == ACTIVE and active_neighbours not in [2, 3]:
            new_cube[i][j][k] = INACTIVE
        elif cube[i][j][k] == INACTIVE and active_neighbours == 3:
            new_cube[i][j][k] = ACTIVE

    cube = new_cube
    #print('\t', cycle+1)
    #pprint.pprint(cube)

print(sum(cube[a][b][c] for (a, b, c) in it.product(x_range, y_range, z_range)))
