def dist_function(city):
    n = len(city)
    min_road = [0] * n
    min_road[1] = (city[1] - city[0])
    min_road[2] = (city[2] - city[0])
    for i in range(3, n):
        min_road[i] = min(min_road[i - 1], min_road[i - 2]) + city[i] - city[i - 1]
    print(min_road)


arr = [10, 20, 25, 45, 50, 70, 80, 85]
dist_function(arr)