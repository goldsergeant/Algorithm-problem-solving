import collections
import sys

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1 for _ in range(1 << N)] for _ in range(N)]  # 사람, 방문 비트


def dfs(cur_person, visit_tasks):
    if visit_tasks == (1 << N) - 1:
        return 0
    if dp[cur_person][visit_tasks] != -1:
        return dp[cur_person][visit_tasks]

    dp[cur_person][visit_tasks] = sys.maxsize

    for next_task in range(N):
        if visit_tasks & (1 << next_task) == 0:  # 방문 체크
            dp[cur_person][visit_tasks] = min(dp[cur_person][visit_tasks],
                                              dfs(cur_person + 1,
                                                  visit_tasks | (1 << next_task)) + cost[cur_person + 1][
                                                  next_task])
    return dp[cur_person][visit_tasks]


answer = sys.maxsize
for i in range(N):
    answer = min(answer, dfs(0, 1 << i)+cost[0][i])
print(answer)
