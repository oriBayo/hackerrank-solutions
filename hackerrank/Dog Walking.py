T = int(input())
for t in range(T):
    result = []
    dog = []
    temp = input().split(" ")
    N = (int(temp[0]))
    K = (int(temp[1]))
    for i in range(N):
        dog.append(int(input()))
    dog.sort()
    for i in range(1, N):
        result.append(dog[i]-dog[i-1])
    result.sort()
    sum = 0
    for i in range(N-K):
        sum += result[i]
    print(sum)

