import collections
import sys

n, l, r = map(int, input().split())
people = []
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
answer = 0

def bfs(row, col, visited):
    queue=collections.deque()
    queue.appendleft((row,col))
    visited[row][col]=True
    connect_cities=[(row,col)]
    total_people_count=people[row][col]

    while queue:
        cur_r,cur_c=queue.pop()
        for i in range(4):
            nr = cur_r + dy[i]
            nc = cur_c + dx[i]
            if nr < 0 or nr > n - 1 or nc < 0 or nc > n - 1:
                continue
            if not visited[nr][nc] and l <= abs(people[cur_r][cur_c] - people[nr][nc]) <= r:
                visited[nr][nc]=True
                queue.appendleft((nr,nc))
                connect_cities.append((nr,nc))
                total_people_count+=people[nr][nc]

    for city in connect_cities:
        people[city[0]][city[1]]=total_people_count//len(connect_cities)

    return connect_cities



for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    flag=0
    for row in range(n):
        for col in range(n):
            if not visited[row][col]:
                cities=bfs(row, col, visited)
                if len(cities)>1:
                    flag=1
    if flag==0:
        break
    answer+=1

print(answer)
