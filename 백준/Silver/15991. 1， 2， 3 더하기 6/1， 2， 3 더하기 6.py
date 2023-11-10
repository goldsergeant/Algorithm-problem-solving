import sys

t=int(sys.stdin.readline())
dp=[0]*(100000+1)

dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=2
dp[4]=3
dp[5]=3
numbers=[]
for _ in range(t):
    numbers.append(int(sys.stdin.readline()))

for i in range(6,max(numbers)+1):
    dp[i]=(dp[i-2]+dp[i-4]+dp[i-6])%1000000009


for num in numbers:
    print(dp[num])