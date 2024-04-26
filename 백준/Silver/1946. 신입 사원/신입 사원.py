import collections
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    scores = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(N))
    scores.sort(key=lambda x: x[0])
    cnt=0
    max_score=scores[0][1]
    for i in range(1,len(scores)):
        if scores[i][1]<max_score:
            max_score=scores[i][1]
        else:
            cnt+=1

    print(N-cnt)