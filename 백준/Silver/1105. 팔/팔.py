import sys

l,r=map(list,sys.stdin.readline().split())
if len(l)!=len(r):
    print(0)
    exit()
answer=0

for i in range(len(r)):
    first=l[i]
    second=r[i]
    if first=='8' and second=='8':
        answer+=1

    elif first!=second:
        break

print(answer)