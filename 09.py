import sys
from collections import deque

def is_valid(last_25, x):
    for i in range(len(last_25) - 1):
        for j in range(i+1, len(last_25)):
            if last_25[i] != last_25[j] and last_25[i] + last_25[j] == x:
                return True
    return False

preamble = deque([int(input()) for _ in range(25)])

for line in sys.stdin:
    number = int(line)
    if not is_valid(preamble, number):
        print(number)
        break
    else:
        preamble.popleft()
        preamble.append(number)
