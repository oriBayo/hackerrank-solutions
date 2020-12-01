t = int(input())

for i in range(t):
    brush1 = 0
    brush2 = 0
    changes = 0
    num_color = int(input())
    colors = input()
    colors = colors.split(" ")
    for k in range(num_color):
        colors[k] = int(colors[k])

    for j in range(num_color):
        searchList = colors[j:]

        if (searchList[0] == brush1) or (searchList[0] == brush2):
            continue
        place1 = -1
        place2 = -1
        brush1_change = False
        brush2_change = False
        try:
            place1 = searchList.index(brush1)
        except ValueError:
            brush1_change = True
        try:
            place2 = searchList.index(brush2)
        except ValueError:
            brush2_change = True

        if (brush1_change == False) and (brush2_change == False):
            if place1 > place2:
                brush1_change = True
            else:
                brush2_change = True
        if brush1_change:
            brush1 = searchList[0]
            changes += 1
            continue
        if brush2_change:
            brush2 = searchList[0]
            changes += 1

    print(changes)
