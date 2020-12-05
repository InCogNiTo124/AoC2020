def get_row_col(position):
    row = 64
    row_mul = 64
    col = 4
    col_mul = 4
    for i in range(7):
        row += (row_mul/2) * (-1 if position[i] == 'F' else 1)
        row_mul //= 2
    for i in range(3):
        col += (col_mul/2) * (-1 if position[i+7] == 'L' else 1)
        col_mul //= 2
    return int(row-0.5), int(col-0.5)

positions = []
try:
    while True:
        position = get_row_col(input().strip())
        positions.append(position)
except:
    pass

print(max(row*8+col for row, col in positions))
