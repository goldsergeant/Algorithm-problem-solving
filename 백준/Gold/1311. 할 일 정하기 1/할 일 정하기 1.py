import sys


def convert_task_to_bit(task):
    return 1 << task


N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dp = [[sys.maxsize for _ in range(1 << N)] for _ in range(N)]  # 사람,일 비트

for task in range(N):
    task_bit = convert_task_to_bit(task)
    dp[0][task_bit] = min(dp[0][task_bit], costs[0][task])

for i in range(1,N):
    for bit in range(1,1<<N):
        if dp[i-1][bit]!=sys.maxsize:
            for task in range(N):
                task_bit = convert_task_to_bit(task)
                if not bit & task_bit:
                    dp[i][bit|task_bit]=min(dp[i][bit|task_bit],dp[i-1][bit]+costs[i][task])

print(dp[-1][-1])