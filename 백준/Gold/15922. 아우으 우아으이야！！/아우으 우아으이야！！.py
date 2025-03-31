import sys

N=int(sys.stdin.readline())
answer=0
pre_y=-sys.maxsize
for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    if pre_y==-sys.maxsize:
        answer+=y-x
        pre_y=y
    else:
        answer+=max(0,y-max(x,pre_y))
        pre_y=max(y,pre_y)

print(answer)