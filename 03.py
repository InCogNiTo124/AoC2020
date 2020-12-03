forest = []
while True:
    try:
        line = input()
        forest.append(list(line))
    except:
        break

move_x, move_y = 3, 1
start_x, start_y = 0, 0
tree_count = 0
for line in forest:
    tree_count += int(line[start_x] == "#")
    start_x = (start_x + move_x) % len(line)
    start_y = (start_y + move_y)
print(tree_count)
