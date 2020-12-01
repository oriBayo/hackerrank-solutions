A2 = [1.880, 1.023, 0.729, 0.577, 0.483, 0.419, 0.373, 0.337, 0.308]

tests = int(input())

for t in range(tests):
    CENTER_LINE = 0
    Rave = 0
    line = input().split()
    size = len(line)
    for i in range(size):
        line[i] = int(line[i])
    element = line[0]
    subgroup = line[1]
    line = line[2:]
    size = len(line)
    x = line.copy()

    n = int((size + subgroup - 1) / subgroup)

    for j in range(n):
        temp = x[:subgroup]
        x = x[subgroup:]
        if len(temp) == 1:
            CENTER_LINE = temp[0]
            Rave = 0
        else:
            CENTER_LINE += sum(temp) / len(temp)
            Rave += (max(temp) - min(temp))

    CENTER_LINE = CENTER_LINE / n
    Rave = Rave / n

    UCL1 = CENTER_LINE + A2[subgroup - 2] * Rave / 3
    UCL2 = CENTER_LINE + A2[subgroup - 2] * Rave * 2 / 3
    UCL3 = CENTER_LINE + A2[subgroup - 2] * Rave
    LCL1 = CENTER_LINE - A2[subgroup - 2] * Rave / 3
    LCL2 = CENTER_LINE - A2[subgroup - 2] * Rave * 2 / 3
    LCL3 = CENTER_LINE - A2[subgroup - 2] * Rave
    SIGMA = (UCL3 - CENTER_LINE) / 3

    in_control = True

    for k in line:
        if k > UCL3 or k < LCL3:
            in_control = False

    for k in range(size - 2):
        count_up = 0
        count_down = 0
        for j in range(3):
            if line[k + j] > UCL2:
                count_up += 1
            if line[k + j] < LCL2:
                count_down += 1

        if count_up >= 2 or count_down >= 2:
            in_control = False

    for k in range(size - 4):
        count_up = 0
        count_down = 0
        for j in range(5):
            if line[k + j] > UCL1:
                count_up += 1
            if line[k + j] < LCL1:
                count_down += 1

        if count_up >= 4 or count_down >= 4:
            in_control = False

    for k in range(size - 7):
        count_up = 0
        count_down = 0
        for j in range(8):
            if line[k + j] > CENTER_LINE:
                count_up += 1
            if line[k + j] < CENTER_LINE:
                count_down += 1

        if count_up == 8 or count_down == 8:
            in_control = False

    if in_control:
        print("In Control")
    else:
        print("Out of Control")