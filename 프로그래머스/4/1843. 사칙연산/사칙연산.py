import sys


def solution(arr):
    min_dp = [[sys.maxsize for _ in range(len(arr))] for _ in range(len(arr))]
    max_dp = [[-sys.maxsize for _ in range(len(arr))] for _ in range(len(arr))]

    def dfs(left, right):
        if left == right:
            return int(arr[left]), int(arr[right])
        if min_dp[left][right] != sys.maxsize and max_dp[left][right] != -sys.maxsize:
            return min_dp[left][right], max_dp[left][right]
        for i in range(left + 1, right, 2):
            opt = arr[i]
            l,r=dfs(left,i-1),dfs(i+1,right)
            min1,max1=l
            min2,max2=r
            if opt=='+':
                min_dp[left][right]=min(min_dp[left][right],min1+min2)
                max_dp[left][right]=max(max_dp[left][right],max1+max2)
            else:
                min_dp[left][right]=min(min_dp[left][right],min1-max2)
                max_dp[left][right]=max(max_dp[left][right],max1-min2)

        return min_dp[left][right], max_dp[left][right]

    return max(dfs(0, len(arr) - 1))


print(solution(["1", "-", "5", "-", "3"]))
print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
