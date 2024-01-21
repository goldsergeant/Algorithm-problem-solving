import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
crops = [int(sys.stdin.readline()) for _ in range(N)]
dp=[[0 for _ in range(N)] for _ in range(N)]

def solve(left,right,depth):
    if left>right:
        return 0
    if left==right:
        dp[left][right]=crops[left]*depth
    if dp[left][right]==0:
        dp[left][right]=max(solve(left+1,right,depth+1)+crops[left]*depth,solve(left,right-1,depth+1)+crops[right]*depth)

    return dp[left][right]

print(solve(0,N-1,1))