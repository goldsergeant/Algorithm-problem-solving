import sys

T, W = map(int, sys.stdin.readline().split())
fruits = [0] + [int(sys.stdin.readline()) for _ in range(T)]
dp = [[[0, 0, 0] for _ in range(W + 1)] for _ in range(T + 1)]


def get_other_side(location):
    return 2 if location == 1 else 1


if fruits[1]==1:
    dp[1][0][1]=1
else:
    dp[1][1][2]=1
for sec in range(2, T + 1):
    location = fruits[sec]
    if location == 1:
        dp[sec][0][1] = dp[sec - 1][0][1] + 1
        dp[sec][0][2] = dp[sec - 1][0][2]
    else:
        dp[sec][0][1] = dp[sec - 1][0][1]
        dp[sec][0][2]=dp[sec-1][0][2]+1

    for move_cnt in range(1, W + 1):
        if location==1:
            dp[sec][move_cnt][1]=max(dp[sec-1][move_cnt-1][2],dp[sec-1][move_cnt][1])+1
            dp[sec][move_cnt][2]=max(dp[sec-1][move_cnt-1][1],dp[sec-1][move_cnt][2])
        else:
            dp[sec][move_cnt][1] = max(dp[sec - 1][move_cnt - 1][2], dp[sec - 1][move_cnt][1])
            dp[sec][move_cnt][2] = max(dp[sec - 1][move_cnt - 1][1], dp[sec - 1][move_cnt][2])+1

answer = 0
for arr in dp[-1]:
    answer = max(answer, max(arr))
print(answer)