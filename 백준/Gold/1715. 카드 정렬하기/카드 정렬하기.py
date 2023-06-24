import heapq
import sys

N=int(input())
cards=[]
answer=0
for _ in range(N):
    heapq.heappush(cards,int(sys.stdin.readline().rstrip()))

if N==1:
    print(0)
    exit()

while cards:
    card1=card2=0
    card1=heapq.heappop(cards)
    if cards:
        card2=heapq.heappop(cards)
    answer+=card1+card2
    if cards:
        heapq.heappush(cards,card1+card2)

print(answer)
