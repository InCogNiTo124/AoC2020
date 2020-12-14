import sys
import re
import itertools as it


def generate_x(count):
    return it.product(*[['0', '1']]*count)

memory = dict()
mask = None
for line in sys.stdin:
    if 'mask' in line:
        mask = line.strip()[7:]
    elif 'mem' in line:
        index, number = re.findall('\d+', line)
        index = "{:b}".format(int(index)).rjust(len(mask), '0')
        for new_x in generate_x(mask.count('X')):
            address = list(index)
            for i, char in enumerate(mask):
                if char == '1' or char == 'X':
                    address[i] = char
            address = "".join(address)
            for char in new_x:
                address = address.replace('X', char, 1)
            memory[int(address, 2)] = int(number)

print(sum(memory.values()))
