inputs = []
while True:
    try:
        x = input().strip()
        left, pw = x.split(': ')
        left, letter = left.split(' ')
        left, right = left.split('-')
        inputs.append((int(left), int(right), letter, pw))
    except:
        break

valid = 0
for x in inputs:
    m, M, letter, pw = x
    if m <= pw.count(letter) <= M:
        valid += 1
print(valid)
