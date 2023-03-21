import collections
import sys

n=int(input())
numbers=list(map(int,sys.stdin.readline().split()))

count=collections.Counter(numbers)
stack=[0]
answer=[-1 for _ in range(n)]
for i in range(1,n):
    while stack and count[numbers[stack[-1]]]<count[numbers[i]]:
        answer[stack.pop()]=numbers[i]
    stack.append(i)
print(*answer)