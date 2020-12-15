numbers = list(map(int, input().strip().split(',')))
cache_dict = dict()
for i, n in enumerate(numbers[:-1], 1):
    cache_dict[n] = i

n = numbers[-1]
for i in range(len(numbers), 30000000):
    if n not in cache_dict:
        number = 0
    else:
        number = i - cache_dict[n]
    cache_dict[n] = i
    n = number
print(n)
