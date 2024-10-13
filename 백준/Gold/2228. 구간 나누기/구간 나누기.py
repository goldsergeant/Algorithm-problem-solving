import sys
from functools import cache

N, M = map(int, sys.stdin.readline().split())
numbers = [0]+list(int(sys.stdin.readline()) for _ in range(N))
t_sum = [0 for _ in range(N+1)]
for i in range(1,N+1):
    t_sum[i]=t_sum[i-1]+numbers[i]

@cache
def dfs(idx, section):
    if section == 0:
        return 0
    if idx < 0:
        return -sys.maxsize

    tmp = dfs(idx - 1, section)
    for i in range(idx,0,-1):
        tmp = max(tmp, dfs(i - 2, section - 1) + t_sum[idx] - t_sum[i - 1])

    return tmp


print(dfs(N, M))
