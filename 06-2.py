import sys

groups = []
s = None
for line in sys.stdin:
    line = line.strip()
    if line == "":
        groups.append(s.copy())
        s = None
    else:
        if s == None:
            s = set(line)
        else:
            s &= set(line)

print(sum(len(t) for t in groups))
