import sys

N, M, L, K = map(int, sys.stdin.readline().split())
stars = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
in_star_cnt=0

for i in range(K):
    for j in range(K):
        x=stars[i][0]
        y=stars[j][1]
        nx=x+L
        ny=y+L
        in_star_cnt=max(in_star_cnt,len(list(filter(lambda u:x<=u[0]<=nx and y<=u[1]<=ny,stars))))

print(K-in_star_cnt)