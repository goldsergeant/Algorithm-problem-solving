import itertools
import sys


N, P, E = map(int, sys.stdin.readline().split())
clients = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
answer=[0 for _ in range(N)]
for idxs in itertools.combinations([i for i in range(N)],P):
    mini,maxi=0,0
    for i in idxs:
        mini+=clients[i][0]
        maxi+=clients[i][1]

    if not (mini<=E<=maxi):
        continue

    diff=E-mini
    for idx in idxs:
        answer[idx]+=clients[idx][0]
        if diff!=0:
            remain_cnt=clients[idx][1]-clients[idx][0]
            if remain_cnt<diff:
                answer[idx]+=remain_cnt
                diff-=remain_cnt
            else:
                answer[idx]+=diff
                diff=0

    print(*answer)
    exit()

print(-1)
