import collections
import sys

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
answer = [-1 for _ in range(n)]
stack = [0]
for i in range(1,n):
    while stack and numbers[stack[-1]]<numbers[i]:
        answer[stack.pop()]=numbers[i]
    stack.append(i)


print(*answer)
