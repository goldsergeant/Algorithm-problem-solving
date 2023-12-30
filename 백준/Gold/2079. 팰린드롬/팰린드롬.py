import sys

st = sys.stdin.readline().rstrip()
dp1 = [[0 for _ in range(len(st))] for _ in range(len(st))]
dp2 = [sys.maxsize] * (len(st)+1)

for i in range(len(st) - 1, -1, -1):
    dp1[i][i] = 1
    for j in range(i + 1, len(st)):
        if j - i == 1 and st[i] == st[j]:
            dp1[i][j] = 1
        else:
            if dp1[i + 1][j - 1] == 1 and st[i] == st[j]:
                dp1[i][j] = 1

dp2[0]=0
for i in range(len(st)):
    for j in range(i+1):
        if dp1[j][i]==1:
            dp2[i+1]=min(dp2[i+1],dp2[j]+1)
        else:
            dp2[i+1]=min(dp2[i+1],dp2[i]+1)

print(dp2[-1])