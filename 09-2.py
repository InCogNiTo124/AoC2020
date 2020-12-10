import sys
from collections import deque

def is_valid(last_25, x):
    for i in range(len(last_25) - 1):
        for j in range(i+1, len(last_25)):
            if last_25[i] != last_25[j] and last_25[i] + last_25[j] == x:
                return True
    return False

numbers = []
preamble = deque([int(input()) for _ in range(25)])
invalid = None
for line in sys.stdin:
    number = int(line)
    numbers.append(number)
    if not is_valid(preamble, number) and invalid is None:
        invalid = number
    else:
        preamble.popleft()
        preamble.append(number)

for i in range(len(numbers)-1):
    for j in range(i, len(numbers)):
        number_range = numbers[i:j+1]
        if sum(number_range) == invalid:
            print(min(number_range) + max(number_range))
