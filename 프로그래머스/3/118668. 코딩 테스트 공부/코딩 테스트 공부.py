from heapq import heappush, heappop
import sys


def solution(alp, cop, problems):
    problems.append([0, 0, 0, 1, 1])
    problems.append([0, 0, 1, 0, 1])
    goal_alp = 0
    goal_cop = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        goal_alp = max(goal_alp, alp_req)
        goal_cop = max(goal_cop, cop_req)

    distance = [[sys.maxsize for _ in range(150 + 1)] for _ in range(150 + 1)]

    heap = [(0, alp, cop)]
    distance[alp][cop] = 0

    while heap:
        cur_cost, cur_alp, cur_cop = heappop(heap)
        if cur_alp >= goal_alp and cur_cop >= goal_cop:
            return cur_cost

        if cur_cost > distance[cur_alp][cur_cop]:
            continue

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            next_alp = min(150, cur_alp + alp_rwd)
            next_cop = min(150, cur_cop + cop_rwd)
            if cur_alp >= alp_req and cur_cop >= cop_req and cur_cost + cost < distance[next_alp][
                next_cop]:
                distance[next_alp][next_cop] = cur_cost + cost
                heappush(heap, (cur_cost + cost, next_alp, next_cop))

print(solution(10, 10, []))
print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
