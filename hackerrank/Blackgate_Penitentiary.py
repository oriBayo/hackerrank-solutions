gang_members = []
height = [0] * 255
num_of_gang_members = int(input())
if not num_of_gang_members:
    exit(0)
for i in range(num_of_gang_members):
    gang = input().split(" ")
    gangster_name, gangster_height = gang[0], int(gang[1])
    if height[gangster_height]:
        height[gangster_height] += [gangster_name]
    elif not height[gangster_height]:
        height[gangster_height] = [gangster_name]

place = 1
for i in range(255):
    if height[i]:
        height[i].sort()
        for j in range(len(height[i])):
            print(height[i][j], end=" ")
        print(f'{place} {len(height[i]) - 1 +place}')
        place += len(height[i])

