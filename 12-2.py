import sys

instructions = [(line[0], int(line[1:])) for line in sys.stdin]

waypoint = 10+1j
ship = 0+0j
for command, move in instructions:
    if command == 'N':
        waypoint += move * 1j
    elif command == 'S':
        waypoint -= move * 1j
    elif command == 'E':
        waypoint += move
    elif command == 'W':
        waypoint -= move
    elif command == 'L':
        waypoint *= 1j**(move // 90)
    elif command == 'R':
        waypoint /= 1j**(move // 90)
    elif command == 'F':
        ship += move * waypoint
print(round(abs(ship.real) + abs(ship.imag)))
