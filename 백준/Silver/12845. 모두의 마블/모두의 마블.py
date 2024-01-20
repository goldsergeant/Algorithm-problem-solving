import sys

N=int(sys.stdin.readline())
cards=list(map(int,sys.stdin.readline().split()))
cards.sort(reverse=True)
score=0
while len(cards)>1:
    score+=cards[0]+cards.pop()

print(score)