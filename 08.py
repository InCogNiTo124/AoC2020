import sys
def cleanup(row):
    command, arg = row.strip().split(' ')
    return command, int(arg)
commands = list(map(cleanup, sys.stdin))

accumulator = 0
PC = 0
visited = set()
while True:
    command, arg = commands[PC]
    if PC in visited:
        print(accumulator)
        break
    else:
        visited.add(PC)
    if command == 'jmp':
        PC += arg
    else:
        PC += 1
        if command == 'acc':
            accumulator += arg
    #print(visited)

