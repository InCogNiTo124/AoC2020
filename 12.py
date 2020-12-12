import sys

instructions = [(line[0], int(line[1:])) for line in sys.stdin]

x = 0+0j
direction = 1+0j

for command, move in instructions:
    if command == 'F':
        x += move * (direction / abs(direction))
    elif command == 'N':
        x += move * 1j
    elif command == 'S':
        x -= move * 1j
    elif command == 'E':
        x += move
    elif command == 'W':
        x -= move
    elif command == 'L':
        direction *= 1j**(move // 90)
    elif command == 'R':
        direction /= 1j**(move // 90)

print(round(abs(x.real) + abs(x.imag)))
