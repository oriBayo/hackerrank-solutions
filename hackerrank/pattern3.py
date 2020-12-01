test = int(input())
for _ in range(test):
    s = input()
    n = len(s)
    count = [0] * (n+1)
    for i in range(1,n):
        j = count[i]
        while j > 0 and s[i] != s[j]:
            j = count[j]
        if s[i] == s[j]:
            count[i+1] = j+1
        else:
            count[i+1] = 0
    print(n - count[n])

