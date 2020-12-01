nums_player = int(input())
players = []
line = input().split()
for i in range(nums_player):
    players.append(int(line[i]))
queries = int(input())
for _ in range(queries):
    q = int(input())
    result = 0
    for p in players:
        if (p & q) == p:
            result = result | p
    if result == q:
        print("YES")
    else:
        print("NO")