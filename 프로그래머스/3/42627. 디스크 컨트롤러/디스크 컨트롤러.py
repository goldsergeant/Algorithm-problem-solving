from heapq import heappush,heappop

def solution(jobs):
    total_times,now,exe_cnt=0,0,0
    start=-1
    heap=[]
    while exe_cnt<len(jobs):
        for req,cost in jobs:
            if start<req<=now:
                heappush(heap,(cost,req))
        
        if heap:
            cost,req= heappop(heap)
            start,now=now,now+cost
            total_times+=(now-req)
            exe_cnt+=1
        else:
            now+=1
    
    return total_times//len(jobs)