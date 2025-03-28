from heapq import heappop,heappush

def solution(food_times, k):
    heap=[]
    l=len(food_times)
    for idx,food_time in enumerate(food_times):
        heappush(heap,(food_time,idx))

    prev_food=0
    while heap:
        food,idx=heap[0]
        t=(food-prev_food)*l
        if k>=t:
            l-=1
            k-=t
            prev_food=food
            heappop(heap)
        else:
            break

    if not heap:
        return -1
    else:
        heap.sort(key=lambda x:x[1])
        return heap[k%l][1]+1