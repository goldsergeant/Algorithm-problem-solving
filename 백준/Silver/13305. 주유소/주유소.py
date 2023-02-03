import sys

n=int(input())
distance=list(map(int,sys.stdin.readline().split()))
oil_price=list(map(int,sys.stdin.readline().split()))
cur_price=oil_price[0]
answer=cur_price*distance[0]
for i in range(1,n-1):
    if cur_price>oil_price[i]:
        cur_price=oil_price[i]
    answer+=cur_price*distance[i]
print(answer)