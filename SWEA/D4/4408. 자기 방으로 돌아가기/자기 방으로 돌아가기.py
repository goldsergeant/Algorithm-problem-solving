import math

T=int(input())
for t in range(1,T+1):
    N=int(input())
    cnt=[0 for _ in range(200+1)]
    for _ in range(N):
        a,b=map(int,input().split())
        a,b=min(a,b),max(a,b)
        a,b=(a+1)//2,(b+1)//2

        for j in range(a,b+1):
            cnt[j]+=1

    print(f'#{t} {max(cnt)}')