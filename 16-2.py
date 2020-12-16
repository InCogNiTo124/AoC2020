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

invalid = []
for ticket in tickets:
    for value in ticket:
        if is_not_valid(value, fields):
            invalid.append(ticket)
            break
for invalid_ticket in invalid:
    tickets.remove(invalid_ticket)

mapping = dict()
for column in range(len(tickets[0])):
    for field, (range1, range2) in fields.items():
        is_valid = True
        for row in range(len(tickets)):
            value = tickets[row][column]
            if not (value in range1 or value in range2):
                is_valid = False
                break
        if is_valid:
            #if column in mapping:
            #    mapping[column].append(field)
            #else:
            #    mapping[column] = [field]
            if field in mapping:
                mapping[field].append(column)
            else:
                mapping[field] = [column]

while sum(len(value) for value in mapping.values()) > len(mapping.keys()):
    determined = set(values[0] for values in mapping.values() if len(values) == 1)
    for possible_fields in mapping.values():
        if len(possible_fields) > 1:
            for found in determined:
                if found in possible_fields:
                    possible_fields.remove(found)

from functools import reduce
import operator as op
print(reduce(op.mul, (my_ticket[i[0]] for key, i in mapping.items() if 'departure' in key)))
