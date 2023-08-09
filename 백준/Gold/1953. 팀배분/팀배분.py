import collections
import sys

n=int(sys.stdin.readline())
dislike=collections.defaultdict(set)
for i in range(1,n+1):
    dislike[i]=list(map(int,sys.stdin.readline()[2:].split()))
white=[]
blue=[]
visited=[False for _ in range(n+1)]

def dfs(node,is_blue):
    if is_blue:
        blue.append(node)
    else:
        white.append(node)

    for hate_person in dislike[node]:
        if not visited[hate_person]:
            visited[hate_person]=True
            dfs(hate_person,not is_blue)


for i in range(1,n+1):
    if not visited[i]:
        visited[i]=True
        dfs(i,True)

blue.sort()
white.sort()
print(len(blue))
print(*blue)
print(len(white))
print(*white)
