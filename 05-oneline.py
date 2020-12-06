import sys

print(max(int(t.strip().replace('F','0').replace('B','1').replace('L', '0').replace('R', '1'), 2) for t in sys.stdin))
