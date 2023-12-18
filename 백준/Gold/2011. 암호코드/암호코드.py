import sys

MOD_NUM = 1000000
password = [0] + list(map(int, sys.stdin.readline().rstrip()))
dp = [0] * len(password)
dp[0],dp[1] = 1,1
for i in range(1, len(password)):
    if password[i] == 0:
        if password[i - 1] == 0 or password[i - 1] >= 3:
            print(0)
            exit()
    if i > 1:
        if 0<password[i]<=26:
            dp[i]+=dp[i-1]
        if 10<=password[i - 1] * 10 + password[i] <= 26:
            dp[i]+=dp[i-2]
        dp[i]%=MOD_NUM
print(dp[-1])