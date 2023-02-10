import sys

reps=int(input())
for _ in range(reps):
    order=1
    n,m=map(int,sys.stdin.readline().split())
    importance=list(map(int,sys.stdin.readline().split()))
    while len(importance)>0:
        if importance[0]==max(importance): #출력하는 경우
            if m==0:
                print(order)
                break
            else:
                importance.pop(0)
                order+=1
                m-=1
        else:
            importance.append(importance.pop(0))
            if m==0:
                m=len(importance)-1
            else:
                m-=1
