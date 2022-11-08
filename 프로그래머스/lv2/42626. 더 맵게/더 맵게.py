import heapq
def solution(scoville, K):
    reps = 0
    if K==0:
        return 0
    heapq.heapify(scoville)
    while len(scoville)>1:
        food1=heapq.heappop(scoville)
        if food1>=K:
            return reps
        food2=heapq.heappop(scoville)
        new_food=food1+food2*2            
        reps+=1
        heapq.heappush(scoville,new_food)
    return reps if min(scoville)>=K else -1