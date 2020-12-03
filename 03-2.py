forest = []
while True:
    try:
        line = input()
        forest.append(list(line))
    except:
        break

for move_x, move_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    start_x, start_y = 0, 0
    tree_count = 0
    for i in range(0, len(forest), move_y):
        line = forest[i]
        tree_count += int(line[start_x] == "#")
        start_x = (start_x + move_x) % len(line)
        start_y = (start_y + move_y)
    print(tree_count)
