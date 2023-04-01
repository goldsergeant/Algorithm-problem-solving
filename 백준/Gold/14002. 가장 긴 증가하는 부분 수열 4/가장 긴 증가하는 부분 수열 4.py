import collections
import sys

n=int(input())
numbers=list(map(int,sys.stdin.readline().split()))
dp=[1 for _ in range(n)]
max_num=0
dic=collections.defaultdict(list)
dic[0].append(numbers[0])

for i in range(1,n):
    for j in range(i):
        if numbers[i]>numbers[j]:
            dp[i]=max(dp[i],dp[j]+1)

order=max(dp)
answer=collections.deque()
for i in reversed(range(n)):
    if dp[i]==order:
        answer.appendleft(numbers[i])
        order-=1

print(max(dp))
print(*answer)
