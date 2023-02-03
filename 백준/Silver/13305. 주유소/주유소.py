import sys

n=int(input())
distance=list(map(int,sys.stdin.readline().split()))
oil_price=list(map(int,sys.stdin.readline().split()))
answer=0
for i in range(n-1):
    if oil_price[i]==min(oil_price[0:n-1]):
        answer+=oil_price[i]*sum(distance[i:n])
        break
    else:
        answer+=oil_price[i]*distance[i]
print(answer)