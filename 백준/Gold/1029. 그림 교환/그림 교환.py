import sys

N=int(sys.stdin.readline())
prices=[list(map(int,list(sys.stdin.readline().strip()))) for _ in range(N)]
dp=[[[0 for _ in range(1<<N)] for _ in range(9+1)] for _ in range(N)] # 마지막 사람, 마지막 가격, 비트

dp[0][0][1]=1
answer=1

for bit in range(1<<N):
    for i in range(N):
        i_bit=1<<i
        for j in range(N):
            j_bit=1<<j
            for p in range(9+1):
                if dp[i][p][bit]==0:
                    continue
                if bit&i_bit and bit&j_bit==0 and p<=prices[i][j]:
                    n_bit=bit|j_bit
                    dp[j][prices[i][j]][n_bit]=max(dp[j][prices[i][j]][n_bit],dp[i][p][bit]+1)

for i in range(N):
    for p in range(9+1):
        answer=max(answer,max(dp[i][p]))

print(answer)