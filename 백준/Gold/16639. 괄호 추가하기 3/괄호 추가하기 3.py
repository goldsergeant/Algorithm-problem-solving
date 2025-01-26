import sys

N = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

max_dp = [[-sys.maxsize for _ in range(N)] for _ in range(N)]
min_dp = [[sys.maxsize for _ in range(N)] for _ in range(N)]


def dfs(left, right):
    if left == right:
        return int(string[left]), int(string[left])
    if max_dp[left][right] != -sys.maxsize and min_dp[left][right] != sys.maxsize:
        return max_dp[left][right], min_dp[left][right],

    for i in range(left + 1, right, 2):
        l,r=dfs(left,i-1),dfs(i+1,right)
        min1,max1,min2,max2 = l[0],l[1],r[0],r[1]
        opt=string[i]
        res=[]
        res.append(eval(f'{min1}{opt}{min2}'))
        res.append(eval(f'{min1}{opt}{max2}'))
        res.append(eval(f'{max1}{opt}{min2}'))
        res.append(eval(f'{max1}{opt}{max2}'))

        res.sort()
        max_dp[left][right]=max(max_dp[left][right],res[-1])
        min_dp[left][right]=min(min_dp[left][right],res[0])

    return max_dp[left][right],min_dp[left][right]

print(max(dfs(0,N-1)))