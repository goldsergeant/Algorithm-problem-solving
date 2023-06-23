import sys

N,M=map(int,input().split())
meats=[]
answer=sys.maxsize

for _ in range(N):
    meats.append(list(map(int,sys.stdin.readline().split())))

meats.sort(key=lambda x:x[0],reverse=True)
meats.sort(key=lambda x:x[1])

cur_weight=0
cur_price=0

for i in range(N):
    w,c=meats[i]

    cur_weight+=w

    if i>=1 and c==meats[i-1][1]: #같은 가격의 고기를 여러개 사는 경우
        cur_price+=c

    else:
        cur_price=c

    if cur_weight>=M:
        answer=min(answer,cur_price)


print( answer if answer!=sys.maxsize else -1)



