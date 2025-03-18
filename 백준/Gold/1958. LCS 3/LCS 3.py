import sys

string1=sys.stdin.readline().strip()
string2=sys.stdin.readline().strip()
string3=sys.stdin.readline().strip()
dp=[[[0 for _ in range(len(string3)+1)] for _ in range(len(string2)+1)] for _ in range(len(string1)+1)]
answer=0
for i in range(1,len(string1)+1):
    for j in range(1,len(string2)+1):
        for k in range(1,len(string3)+1):
            if string1[i-1]==string2[j-1]==string3[k-1]:
                dp[i][j][k]=dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
            answer=max(answer,dp[i][j][k])

print(answer)