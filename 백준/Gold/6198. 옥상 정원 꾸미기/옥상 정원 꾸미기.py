import sys

N=int(sys.stdin.readline())
stack=[]
answer=0
for i in range(N):
    building=int(sys.stdin.readline())
    if not stack:
        stack.append((i,building))
        continue

    while stack and stack[-1][1]<=building:
        stack.pop()

    answer+=len(stack)
    stack.append((i, building))

print(answer)