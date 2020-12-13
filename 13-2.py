_ = input()
table = input().strip().split(',')
buses = list(filter(lambda x: x != 'x', table))
buses = sorted(list(map(int, buses)), reverse=True) # sorting speed things up
indices = list(map(lambda t: -table.index(str(t)), buses))
start = indices[0]
d = buses[0]
i = 0
while i < len(indices)-1:
    start += d
    if (start - indices[i+1]) % buses[i+1] == 0:
        d *= buses[i+1]
        i +=  1
print(start)
