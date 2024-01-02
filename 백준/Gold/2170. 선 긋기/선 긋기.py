import sys

N=int(sys.stdin.readline())
answer=0
lines=[]
for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    lines.append((x,y))

lines.sort()
answer=lines[0][1]-lines[0][0]
last_end=lines[0][1]
for line in lines[1:]:
    x,y=line
    if x>=last_end:
        answer+=(y-x)
    else:
        answer+=max((y-x)-(last_end-x),0)
    last_end=max(last_end,y)

print(answer)

