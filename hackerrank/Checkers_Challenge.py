arr = []
x = []
t = 1
for k in range(t):
    for i in range(8):
        temp = input().split()
        arr.extend(temp)
    for word in arr:
      word=list(word)
    print(arr)
#     for i in range(8):
#         for j in range(8):
#             if arr[i][j] == 'o':
#                 start = (i, j)
#             if arr[i][j] == 'x':
#                 x.append((i, j))
# print("start ",start,'x ',x)
# .......o
# .x.x.x..
# xxxx.xx.
# ........
# ........
# .x.xx..x
# x.......
# ..x...x.
