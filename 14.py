import sys
import re

memory = dict()
mask = None
for line in sys.stdin:
    if 'mask' in line:
        mask = line.strip()[7:]
    elif 'mem' in line:
        index, number = re.findall('\d+', line)
        number = list("{:b}".format(int(number)).rjust(len(mask), '0'))
        for i in range(len(mask)):
            if mask[i] == '1':
                number[i] = '1'
            elif mask[i] == '0':
                number[i] = '0'
        memory[int(index)] = int(''.join(number), 2)

print(sum(memory.values()))
