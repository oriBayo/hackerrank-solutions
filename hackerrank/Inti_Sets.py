M = 1000000007



def power(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n
    if p % 2:
        return (n % M * power(n,p-1) % M) % M
    r = power(n,p/2)
    return (r % M * r % M) % M


TOW = power(2, M - 2) % M


# Divides the number by primary factors
def factors(num):
    f = []
    for i in range(2, num):
        if num % i == 0:
            f.append(i)
            while num % 2 == 0:
                num /= i
    if num > 1 and num not in f:
        f.append(num)
    return f


# sum(A,B)= (B(B+1))/2 - ((A-1)A)/2
# (A*B)%M = (A%M * B%M) %M
def large_sum(a, b):
    return ((b % M * (b + 1) % M) % M * TOW) % M - (((a - 1) % M * a % M) % M * TOW) % M


test = int(input())
for _ in range(test):
    line = input().split()
    N = int(line[0])
    A = int(line[1])
    B = int(line[2])
    ans = large_sum(A, B)
    comp = 0

    fact = factors(N)
    k = len(fact)

    for mask in range(1 << k):
        m = 1
        cnt = 0

        for i in range(k):
            if (mask & (1 << i)) != 0:
                cnt += 1
                m *= fact[i]

        if cnt == 0:
            continue

        a = int((A + m - 1) / m)
        b = int(B / m)
        r = (large_sum(a, b) * (m % M)) % M
        if cnt % 2 == 0:
            comp = (comp % M - r % M + M) % M
        else:
            comp = (comp % M + r % M) % M

    print(int((ans % M - comp % M + M) % M))
