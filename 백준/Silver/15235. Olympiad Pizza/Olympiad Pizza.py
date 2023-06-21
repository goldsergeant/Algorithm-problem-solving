import collections

N=int(input())
answer=[0 for i in range(N)]
arr=list(map(int,input().split()))
deq=collections.deque([[arr[i],i] for i in range(len(arr))])

while deq:
    for i in deq:
        answer[i[1]]+=1
    element=deq.popleft()
    element[0]-=1
    if element[0]>0:
        deq.append(element)

print(*answer)