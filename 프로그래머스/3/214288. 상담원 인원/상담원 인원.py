import sys
from heapq import heappush, heappop

def dfs(n, k, total):
    if len(participants) == k:
        if total == n:
            cases.append(participants.copy())
        return

    for cnt in range(1, (n - total) + 1):
        participants.append(cnt)
        dfs(n, k, total + cnt)
        participants.pop()


def solution(k, n, reqs):
    global cases,participants
    cases = []
    participants = []
    def get_ready_time(case):
        total_ready_time = 0
        heaps = [[] for _ in range(k + 1)]
        for start, during, category in reqs:
            while heaps[category] and heaps[category][0] <= start:
                heappop(heaps[category])

            if len(heaps[category]) < case[category]:
                heappush(heaps[category], start + during)
                continue

            if heaps[category]: # 기다려야 할 때
                ready_time=heappop(heaps[category])-start
                total_ready_time += ready_time
                heappush(heaps[category], start + during+ready_time)
            else: # 안기다려도 될 때
                heappush(heaps[category], start + during)
        return total_ready_time

    answer = sys.maxsize
    dfs(n, k, 0)
    for case in cases:
        answer = min(answer, get_ready_time([0] + case))
    return answer

print(solution(3,5,[[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))
print(solution(	2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))