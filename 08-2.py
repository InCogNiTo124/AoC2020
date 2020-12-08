import sys
def cleanup(row):
    command, arg = row.strip().split(' ')
    return command, int(arg)
commands = list(map(cleanup, sys.stdin))

for i in range(len(commands)):
    command, arg = commands[i]
    if command == 'acc':
        continue
    elif command == 'jmp':
        commands[i] = ('nop', arg)
    else:
        commands[i] = ('jmp', arg)
    accumulator = 0
    PC = 0
    visited = set()
    while True:
        try:
            command, arg = commands[PC]
        except IndexError:
            print(accumulator)
            break

        if PC in visited:
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
    command, arg = commands[i]
    if command == 'acc':
        continue
    elif command == 'jmp':
        commands[i] = ('nop', arg)
    else:
        commands[i] = ('jmp', arg)

