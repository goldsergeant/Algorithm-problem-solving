from heapq import heappush,heappop
def solution(n, works):
    answer = 0
    heap=[]
    
    for work in works:
        heappush(heap,(-work,work))
        
    for _ in range(n):
        if not heap:
            break
        minus_value,value=heappop(heap)
        if value==0:
            continue
        heappush(heap,(-(value-1),value-1))
    for minus_value,value in heap:
        answer+=(value**2)
    return answer