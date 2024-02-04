import collections
import sys

N=int(sys.stdin.readline())
bugs=list(map(int,sys.stdin.readline().split()))
answer=0
provider=collections.deque()
consumer=collections.deque()

for idx,cnt in enumerate(bugs):
    if cnt>0:
        provider.append([idx+1,cnt])
    else:
        consumer.append([idx+1,-cnt])

while provider and consumer:
        if provider[0][1]>consumer[0][1]:
            answer += consumer[0][1]*(abs(provider[0][0]-consumer[0][0]))
            provider[0][1]-=consumer[0][1]
            consumer.popleft()
        elif provider[0][1]<consumer[0][1]:
            answer+=provider[0][1]*(abs(provider[0][0]-consumer[0][0]))
            consumer[0][1]-=provider[0][1]
            provider.popleft()
        else:
            answer+=provider[0][1]*(abs(provider[0][0]-consumer[0][0]))
            provider.popleft()
            consumer.popleft()

print(answer)
