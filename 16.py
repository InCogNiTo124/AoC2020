import sys

def is_not_valid(value, conditions):
    return not any((value in range1 or value in range2) for _, (range1, range2) in conditions.items())
        

def make_range(range_proto):
    limits = tuple(int(t) for t in map(int, range_proto.split('-')))
    return range(limits[0], limits[1]+1)

fields = dict()
for _ in range(20):
    field, ranges = input().strip().split(': ')
    range1, _, range2 = ranges.split(' ')
    range1 = make_range(range1)
    range2 = make_range(range2)
    fields[field] = [range1, range2]

input()
input()
my_ticket = list(map(int, input().strip().split(',')))
input()
input()
tickets = [tuple(map(int, line.strip().split(','))) for line in sys.stdin]

sum = 0
for ticket in tickets:
    for value in ticket:
        if is_not_valid(value, fields):
            sum += value
print(sum)
