def score(card1, card2):
    if card1 == 'R' and card2 == 'R':
        return 50
    if card1 == 'R':
        if card2 == 'T':
            return 10
        elif card2 in ['J', 'Q', 'K']:
            return 15
        elif card2 == 'A':
            return 20
        else:
            return int(card2)
    if card2 == 'R':
        if card1 == 'T':
            return 10
        elif card1 in ['J', 'Q', 'K']:
            return 15
        elif card1 == 'A':
            return 20
        else:
            return int(card1)
    if card1 == 'T':
        return 10
    elif card1 in ['J', 'Q', 'K']:
        return 15
    elif card1 == 'A':
        return 20
    else:
        return int(card1)

result = []
num_card = int(input())
while num_card:
    A = [0]
    B = [0]
    R = [([0]*(num_card+1)) for i in range(num_card+1)]
    line = input().split()
    for i in range(num_card):
        A.append(line[i])
    line = input().split()
    for i in range(num_card):
        B.append(line[i])
    for i in range(1, num_card + 1):
        for j in range(1, num_card + 1):
            R[i][j] = max(R[i][j - 1], R[i - 1][j])
            if A[i] == B[j] or A[i] == 'R' or B[j] == 'R':
                R[i][j] = max(R[i][j], R[i - 1][j - 1] + score(A[i], B[j]))
    result .append(int(R[num_card][num_card] * 2))
    num_card = int(input())

for r in result:
    print(r)