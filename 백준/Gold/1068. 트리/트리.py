import collections
import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
tree=collections.defaultdict(list)
target=int(input())
answer=0
root=0
for i in range(len(arr)):
    if arr[i]==-1:
        root=i
        continue
    tree[arr[i]].append(i)

q=collections.deque([root])
while q:
    node = q.pop()
    if node!=target:
        flag=0
        for next_node in tree[node]:
            if next_node!=target:
                flag=1
                q.appendleft(next_node)
        if flag==0:
            answer+=1
print(answer)
