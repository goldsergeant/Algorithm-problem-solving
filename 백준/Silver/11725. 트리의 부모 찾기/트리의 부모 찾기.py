import collections
import sys


n=int(input())
graph=collections.defaultdict(list)
parents=[0 for i in range(n+1)]
for _ in range(n-1):
    parent,child=map(int,sys.stdin.readline().split())
    graph[parent].append(child)
    graph[child].append(parent)

stack=collections.deque()
stack.append(1)
while stack:
    next=stack.pop()
    for i in graph[next]:
        if parents[i]==0:
            parents[i]=next
            stack.append(i)
for i in range(2,len(parents)):
    print(parents[i])