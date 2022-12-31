import collections

n=int(input())
con=(int(input()))
visited=[]
graph=collections.defaultdict(list)
for i in range(con):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(num):
    if num not in visited:
        visited.append(num)
    else:
        return
    for node in graph[num]:
        dfs(node)

dfs(1)
print(len(visited)-1)
