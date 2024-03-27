import collections
import sys

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
answer=[]
for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

K=int(sys.stdin.readline())
destroyed_cities=set(list(map(int,sys.stdin.readline().split())))

bomb_cities=set()
for city in destroyed_cities:
    temp={city}
    answer.append(city)
    for adj_city in graph[city]:
        if adj_city not in destroyed_cities:
            temp.clear()
            answer.pop()
            break
        else:
            temp.add(adj_city)

    bomb_cities.update(temp)
    if len(bomb_cities)==len(destroyed_cities):
        print(len(answer))
        print(*sorted(answer))
        exit()

print(-1)
