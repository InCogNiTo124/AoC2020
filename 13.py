import re

def is_not_rel_prime(num, num_list):
    for n in num_list:
        if num % n == 0:
            return True, n
    return False, -1

time = int(input())
buses = input()
buses = list(map(int, re.findall('\d+', buses)))

for number in range(time, time + min(buses)):
    does_divide, divisor = is_not_rel_prime(number, buses)
    if does_divide:
        print((number - time) * divisor)
        break

