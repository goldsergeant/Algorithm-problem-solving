import sys
from heapq import heappop,heappush
N = int(sys.stdin.readline())
tournament = [int(sys.stdin.readline()) for _ in range(N)]
heap=[]
for power in tournament:
    heappush(heap,power)

answer=0
while len(heap)>1:
    worst_val=heappop(heap)
    worst_idx=tournament.index(worst_val)
    if worst_idx==0:
        right=tournament[worst_idx+1]
        answer+=abs(worst_val-right)
    elif worst_idx==len(tournament)-1:
        left=tournament[worst_idx-1]
        answer+=abs(worst_val-left)
    else:
        left=tournament[worst_idx-1]
        right=tournament[worst_idx+1]
        answer+=min(abs(worst_val-left),abs(worst_val-right))
    tournament.pop(worst_idx)
print(answer)