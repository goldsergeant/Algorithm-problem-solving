import heapq
import sys

n=int(sys.stdin.readline())
total_cnt=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
q=[]
for i in range(len(numbers)):
    flag=0
    for j in range(len(q)):
        if q[j][2]==numbers[i]:
            q[j][0]+=1
            flag=1
    if flag==1:
        continue

    if len(q)==n:
        q.sort(key=lambda x:(x[0],x[1]))
        q.pop(0)
        
    q.append([1,i,numbers[i]])

q.sort(key=lambda x:x[2])
print(*[i[2] for i in q])
