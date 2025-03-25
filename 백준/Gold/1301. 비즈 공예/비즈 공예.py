import sys
from functools import cache

N = int(sys.stdin.readline())
marbles = list(int(sys.stdin.readline()) for _ in range(N))
while len(marbles)<5:
    marbles.append(0)
total_marbles=sum(marbles)
answer = 0

@cache
def dfs(marble_position, next1, next2, x,y,z,p,q):
    if marble_position == 0:
        return 1

    case=0
    for i in range(N):
        if next1 ==i or next2 ==i:
            continue
        if i==0 and x>0:
            case += dfs(marble_position - 1, i, next1, x-1, y, z, p, q)

        elif i==1 and y>0:
            case += dfs(marble_position - 1, i, next1, x, y-1, z, p, q)

        elif i==2 and z>0:
            case += dfs(marble_position - 1, i, next1, x, y, z-1, p, q)
        elif i==3 and p>0:
            case += dfs(marble_position - 1, i, next1, x, y, z, p-1, q)
        elif i==4 and q>0:
            case += dfs(marble_position - 1, i, next1, x, y, z, p, q-1)

    return case



print(dfs(total_marbles,N,N,marbles[0],marbles[1],marbles[2],marbles[3],marbles[4]))
