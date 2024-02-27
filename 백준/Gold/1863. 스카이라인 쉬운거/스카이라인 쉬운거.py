import sys

N = int(sys.stdin.readline())
stack = []
answer = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    while stack and stack[-1] > y:
        stack.pop()
        answer += 1
    if stack and stack[-1] == y:
        continue
    if y!=0:
        stack.append(y)

while stack:
    stack.pop()
    answer += 1

print(answer)
