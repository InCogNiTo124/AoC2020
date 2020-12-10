import sys

adapters = [0] + sorted([int(line.strip()) for line in sys.stdin])

x = [1] + [0 for _ in range(max(adapters))]
for i in adapters:
    for j in range(1, 3+1):
        if i - j in adapters:
            x[i] += x[i-j]

print(x[-1])
