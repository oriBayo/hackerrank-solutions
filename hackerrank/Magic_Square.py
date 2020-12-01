size = int(input())
matrix = []
result = []
for i in range(size):
    num = input().split()
    for j in range(size):
        num[j] = int(num[j])
    matrix.append(num)

main_diagonal = 0

for i in range(size):
    main_diagonal += matrix[i][i]

antidiagonal = 0

for i in range(size):
    antidiagonal += matrix[i][size-1-i]
if antidiagonal != main_diagonal:
    result.append(0)

for i in range(size):
    sum_rows = 0
    sum_columns = 0
    for j in range(size):
        sum_rows += matrix[i][j]
        sum_columns += matrix[j][i]
    if sum_rows != main_diagonal:
        result.append(i+1)
    if sum_columns != main_diagonal:
        result.append((i+1)*-1)

result.sort()
print(len(result))
for r in result:
    print(r)