import numpy as np

rows, columns = input().split()
rows = int(rows)
columns = int(columns)
canvas = np.zeros((rows, columns))
arr = []
n = int(input())
for i in range(n):
    arr.append(input())

for k in arr:
    line = k.split()
    operation = line[0]
    top_left_row = int(line[1])
    top_left_column = int(line[2])
    bottom_right_row = int(line[3])
    bottom_right_column = int(line[4])

    if operation == 'a':
        canvas[top_left_row-1:bottom_right_row, top_left_column-1:bottom_right_column] += 1
    elif operation == 'r':
        canvas[top_left_row - 1:bottom_right_row, top_left_column - 1:bottom_right_column] += -1
    else:
        sum_blocks = sum(sum(canvas[top_left_row - 1:bottom_right_row, top_left_column - 1:bottom_right_column]))
        print(int(sum_blocks))
