import sys

dp = [[[0 for i in range(21)] for i in range(21)] for i in range(21)]

def solve(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return solve(20,20,20)
    if dp[a][b][c]!=0:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c]=solve(a, b, c-1) + solve(a, b-1, c-1) - solve(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c]= solve(a-1, b, c) + solve(a-1, b-1, c) + solve(a-1, b, c-1) - solve(a-1, b-1, c-1)
        return dp[a][b][c]


while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break
    print('w(%d, %d, %d) = %d' %(a,b,c,solve(a,b,c)))

