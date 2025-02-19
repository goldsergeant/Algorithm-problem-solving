import sys


def solution(info, n, m):
    answer = sys.maxsize
    info = [[0, 0]] + info
    dp = [[sys.maxsize for _ in range(m)] for _ in range(len(info))]  # 물건 개수, b 흔적 개수
    for i in range(m):
        dp[0][i] = 0

    for i in range(1, len(info)):
        for j in range(m):
            dp[i][j]=min(dp[i][j],dp[i-1][j]+info[i][0])
            if j+info[i][1]<m:
                dp[i][j+info[i][1]]=min(dp[i][j+info[i][1]],dp[i-1][j])

    answer=min(dp[-1])
    return answer if answer<n else -1


print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
print()
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))
print()
print(solution([[3, 3], [3, 3]], 7, 1))
print()
print(solution([[3, 3], [3, 3]], 6, 1))
