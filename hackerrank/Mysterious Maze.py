import queue


def search_neighbors(i, j, m):
    n = len(m[i])
    if i == 0:
        find_way(i, j, m)
    if i + 1 < n:
        if m[i + 1][j] == '+':
            find_way(i, j, m)
    if i - 1 >= 0:
        if m[i - 1][j] == '+':
            find_way(i, j, m)
    if j + 1 < n:
        if m[i][j + 1] == '+':
            find_way(i, j, m)
    if j - 1 >= 0:
        if m[i][j - 1] == '+':
            find_way(i, j, m)


def find_way(i, j, m):
    m[i][j] = '+'
    q = queue.Queue()
    q.put((i, j))
    n = len(m[i])
    while not q.empty():
        if '+' in m[n-1]:
            return
        curr = q.get()
        x = curr[0]
        y = curr[1]
        if x + 1 < n:
            if m[x + 1][y] == 'O':
                q.put((x + 1, y))
                m[x + 1][y] = '+'
        if x - 1 >= 0:
            if m[x - 1][y] == 'O':
                q.put((x - 1, y))
                m[x - 1][y] = '+'
        if y + 1 < n:
            if m[x][y + 1] == 'O':
                q.put((x, y + 1))
                m[x][y + 1] = '+'
        if y - 1 >= 0:
            if m[x][y - 1] == 'O':
                q.put((x + 1, y - 1))
                m[x][y - 1] = '+'


size = int(input())
line = input().split()
maze = [(['X' for j in range(size)]) for i in range(size)]
count = 1
while '-1' not in line:
    x = int(line[0]) - 1
    y = int(line[1]) - 1
    maze[x][y] = 'O'
    search_neighbors(x, y, maze)
    if '+' in maze[-1] :
        print(count)
        exit()
    line = input().split()
    count += 1
print(-1)
