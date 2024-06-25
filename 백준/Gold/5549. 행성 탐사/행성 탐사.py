import collections
import sys



N, M = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
t_sum=[[[0,0,0] for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        for k in range(3):
            t_sum[i][j][k]=t_sum[i-1][j][k]+t_sum[i][j-1][k]-t_sum[i-1][j-1][k]

        if maps[i-1][j-1]=='J':
            t_sum[i][j][0]+=1
        elif maps[i-1][j-1]=='O':
            t_sum[i][j][1]+=1
        elif maps[i-1][j-1]=='I':
            t_sum[i][j][2]+=1

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())

    for i in range(3):
        print(t_sum[c][d][i]-t_sum[c][b-1][i]-t_sum[a-1][d][i]+t_sum[a-1][b-1][i],end=' ')
    print()