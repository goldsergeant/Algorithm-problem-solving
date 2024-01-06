import sys

N=int(sys.stdin.readline())
heights=list(map(int,sys.stdin.readline().split()))
answer=[-1]
stack=[]
for idx,height in enumerate(heights):
    if not stack:
        stack.append((idx,height))
        continue

    while stack and stack[-1][1]<=height:
        stack.pop()

    if not stack:
        answer.append(-1)
    else:
        answer.append(stack[-1][0])

    stack.append((idx,height))

print(*map(lambda x:x+1,answer))