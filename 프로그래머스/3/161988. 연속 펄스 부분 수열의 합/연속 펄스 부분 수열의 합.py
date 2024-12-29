import sys

def solution(sequence):
    answer = 0
    dp=[[-sys.maxsize for _ in range(2)] for _ in range(len(sequence))]
    dp[0][0]=sequence[0]
    dp[0][1]=-sequence[0]
    
    for i in range(1,len(sequence)):
        dp[i][0]=max(sequence[i],dp[i-1][1]+sequence[i])
        dp[i][1]=max(-sequence[i],dp[i-1][0]-sequence[i])
    
    for i in range(len(sequence)):
        answer=max(answer,max(dp[i]))
        
    return answer