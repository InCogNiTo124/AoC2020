import sys

groups = []
s = set()
for line in sys.stdin:
    line = line.strip()
    if line == "":
        groups.append(s.copy())
        s = set()
    else:
        s |= set(line)

print(sum(len(t) for t in groups))
