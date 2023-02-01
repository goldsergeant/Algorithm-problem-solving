import collections

n=int(input())
queue=collections.deque([i for i in range(1,n+1)])
index=0
while len(queue)>1:
    if index%2==0:
        queue.popleft()
    else:
        temp=queue.popleft()
        queue.append(temp)
    index+=1
print(queue[0])