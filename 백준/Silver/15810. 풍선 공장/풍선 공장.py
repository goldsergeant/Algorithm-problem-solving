import heapq
import sys

n,m=map(int,sys.stdin.readline().split())
time_arr=list(map(int,sys.stdin.readline().split()))
balloon_cnt=0
q=[]
for i in range(len(time_arr)):
    heapq.heappush(q,(time_arr[i],i))

while q:
    cur_time,idx=heapq.heappop(q)
    balloon_cnt+=1
    if balloon_cnt==m:
        print(cur_time)
        break
    heapq.heappush(q,(cur_time+time_arr[idx],idx))