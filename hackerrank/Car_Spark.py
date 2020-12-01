def opt(intervals):
    optimal = []
    for i in range(len(intervals)):
        place = 0
        for j in range(i):
            if intervals[i][0][0] >= intervals[j][0][1]:
                place = j + 1
        optimal.append(place)
    return optimal


test = int(input())
for _ in range(test):
    interval = []
    lines = []
    number_of_bookings = int(input())
    for k in range(number_of_bookings):
        lines.append(input())

    for line in lines:
        line = line.split()
        start_time = int(line[0])
        end_time = int(line[1])
        amount = int(line[2])
        interval.append([(start_time, end_time), amount])

    interval.sort(key=lambda arr: arr[0][1])
    p = opt(interval)
    result = [0] * (len(interval)+1)

    for j in range(1, len(interval)+1):
        result[j] = max(interval[j-1][1]+result[p[j-1]], result[j-1])
    print(result[-1])
