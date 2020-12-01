numbers = []
while True:
    try:
        numbers.append(int(input()))
    except:
        break

for i in range(len(numbers)-2):
    x = numbers[i]
    for j in range(i, len(numbers)-1):
        y = numbers[j]
        for k in range(j, len(numbers)):
            z = numbers[k]
            if x+y+z == 2020:
                print(x, y, z, x*y*z)
