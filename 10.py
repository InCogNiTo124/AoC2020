import sys

adapters = [0]+sorted([int(line.strip()) for line in sys.stdin])
print(adapters)
ones = 0
threes = 1
for x, y in zip(adapters[:-1], adapters[1:]):
    if y - x == 1:
        ones += 1
    elif y - x == 3:
        threes += 1

print(ones, threes)
print(ones*threes)
