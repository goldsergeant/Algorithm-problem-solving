import sys
sys.setrecursionlimit(1000000)
def solution(n):
    dp=[-1 for _ in range(n+1)]
    def fibo(num):
        if num==0 or num==1:
            return num
        if dp[num]!=-1:
            return dp[num]
        dp[num]=(fibo(num-1)+fibo(num-2))%1234567
        return dp[num]
    
    return fibo(n)