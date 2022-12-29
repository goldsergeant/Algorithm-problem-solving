import collections

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))
queue = collections.deque([[0, 0, 1]])
while queue:
    point = queue.popleft()
    cur_x, cur_y, distance = point[0], point[1], point[2]
    if cur_x == m - 1 and cur_y == n - 1:
        print(distance)
        exit()
    if cur_y < n - 1:
        if arr[cur_y + 1][cur_x] == 1:
            queue.append([cur_x, cur_y+1, distance + 1])
            arr[cur_y+1][cur_x]=0
    if cur_x < m - 1:
        if arr[cur_y][cur_x + 1] == 1:
            queue.append([cur_x+1, cur_y, distance + 1])
            arr[cur_y][cur_x+1]=0
    if cur_y > 0:
        if arr[cur_y - 1][cur_x] == 1:
            queue.append([cur_x, cur_y-1, distance + 1])
            arr[cur_y-1][cur_x]=0
    if cur_x > 0:
        if arr[cur_y][cur_x - 1] == 1:
            queue.append([cur_x-1, cur_y, distance + 1])
            arr[cur_y][cur_x-1]=0
