T=int(input())
for _ in range(T):
    N=int(input())
    stocks=list(map(int,input().split()))
    profit=0

    i=len(stocks)-1

    while i>0:
        ex=stocks[i]
        while i>0:
            i-=1
            if ex>stocks[i]:
                profit+=(ex-stocks[i])
            else:
                break

    print(profit)
