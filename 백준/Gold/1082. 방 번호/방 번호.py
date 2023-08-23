import collections
import sys

n=int(input())
p=list(map(int,input().split()))
m=int(input())
spent_money=0
answer=[]

min_idx=p.index(min(p))
if min_idx==0:
    if n==1:
        print(0)
        exit()
    min_idx_not0=p.index(min(p[1:]))
    if m<p[min_idx_not0]:
        print(0)
        exit()

    answer.append((min_idx_not0,p[min_idx_not0]))
    spent_money+=p[min_idx_not0]

while spent_money+p[min_idx]<=m:
    answer.append((min_idx,p[min_idx]))
    spent_money+=p[min_idx]

for i in range(len(answer)):
    room,price=answer[i]
    for j in range(n-1,-1,-1):
        if spent_money+p[j]-price<=m:
            answer[i]=(j,p[j])
            spent_money+=(p[j]-price)
            break

print(''.join(str(i[0]) for i in answer))

