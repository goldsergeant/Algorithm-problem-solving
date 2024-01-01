import collections
import math
import sys

T = int(sys.stdin.readline())

def game(left,right,turn):
    if left>right:
        return 0
    if dp[left][right]==0:
        if turn%2==0: # 근우
            dp[left][right]=max(cards[left]+game(left+1,right,turn+1),cards[right]+game(left,right-1,turn+1))
        else: # 명우
            dp[left][right]=min(game(left+1,right,turn+1),game(left,right-1,turn+1))

    return dp[left][right]

for _ in range(T):
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    dp=[[0 for _ in range(N)] for _ in range(N)]
    game(0,N-1,0)
    print(dp[0][N-1])