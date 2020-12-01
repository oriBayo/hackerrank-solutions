import numpy as np

MAX_LENGTH = 510
MAX_N = 1000000007
# p = np.zeros((MAX_N, int(MAX_LENGTH / 2), int(MAX_LENGTH / 2)))
test = int(input())
for _ in range(test):

    line = input().split()
    n = int(line[0])
    s = line[1]
    length = len(s)
    middle = int((length + 1) / 2)
    not_match = 0
    p = np.zeros((MAX_N, int(MAX_LENGTH / 2), int(MAX_LENGTH / 2)),dtype=np.uint8)

    for i in range(middle):
        if s[i] != s[length - i - 1]:
            not_match += 1

    p[0][0][0] = 1

    for i in range(n + 1):
        for j in range(1, middle + 1):
            for k in range(not_match + 1):

                if j - 1 == length - j:
                    p[i][j][k] = p[i][j - 1][k]
                    if n >= 1:
                        p[i][j][k] = (p[i][j][k] + 25 * p[n - 1][j - 1][k])

                elif s[j-1] == s[length - j]:
                    p[i][j][k] = p[i][j - 1][k]
                    if n >= 2:
                        p[i][j][k] = (p[i][j][k] + 25 * p[i - 2][j - 1][k])

                elif s[j-1] != s[length - j]:
                    if k >= 1 and i >= 1:
                        p[i][j][k] = 2 * p[i - 1][j - 1][k - 1]
                    if i >= 2:
                        p[i][j][k] = p[i][j][k] + 24 * p[i - 2][j - 1][k - 1]
    print(int(p[n][middle][not_match]))
