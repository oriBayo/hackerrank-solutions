problem = []
SYMBOLS = {}

for _ in range(5):
    problem.append(input())
BASE, basic_literature = problem[0].split()
BASE = int(BASE)
basic_literature = list(basic_literature)
for i in range(BASE):
    SYMBOLS[basic_literature[i]] = i
A = list(problem[1][1:])
B = list(problem[2][1:])
SYMBOLS[' '] = 0

result = [0] * (len(A)+1)
remainder = 0


for i in range(len(A) - 1, -1, -1):
    a = SYMBOLS[A[i]]
    b = SYMBOLS[B[i]]
    sum = a + b + remainder
    remainder = sum // BASE
    sum %= BASE
    result[i+1] = basic_literature[sum]

if result[0] == 0:
    result[0] = ' '

problem[4] = listToStr = ''.join(map(str, result))

for p in problem:
    print(p)
