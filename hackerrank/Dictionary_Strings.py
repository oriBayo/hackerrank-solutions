words = []
dicts = []
monim = [0] * 26
test = int(input())
for t in range(test):
    num_words, num_dict = input().split()
    num_words = int(num_words)
    num_dict = int(num_dict)
    for i in range(num_words):
        word = input()
        words.append(word)
    for i in range(num_dict):
        dict_w = input()
        dicts .append(dict_w)

# create monim array
    for word in words:
        for i in range(len(word)):
            num = word.count(word[i])
            if monim[ord(word[i]) - ord('a')] < num:
                monim[ord(word[i]) - ord('a')] = num

    for d in dicts:
        count = 0
        flag = 0
        for i in range(26):
            if d.count(chr(i+ord('a'))) < monim[i]:
                count += 1
                flag = 1
            d = d.replace(chr(i + ord('a')), "", monim[i])
            if d == "" and flag == 0:
                break

        if flag == 1:
            print('No',count)
        elif d == "":
            print('Yes Yes')
        elif d != "":
            print('Yes No')




