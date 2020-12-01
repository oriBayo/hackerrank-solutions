def func(st, n, m, s, t):

    if st == n:
        return t

    temp = int((st + n)/2 + (st + n) % 2)
    t += (temp-st) * m + s
    return func(temp, n, m, s, t)


N, M, S = input().split()
N = int(N)
M = int(M)
S = int(S)
start = 1
print(func(start, N, M, S, 0))
