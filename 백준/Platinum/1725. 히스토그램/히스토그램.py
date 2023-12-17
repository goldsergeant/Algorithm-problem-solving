import sys

N = int(sys.stdin.readline())
stack = []
answer = 0
for i in range(N):
    cur_height = int(sys.stdin.readline())
    if not stack:
        stack.append((i, cur_height))
        continue

    while stack and stack[-1][1] > cur_height:
        idx, height = stack.pop()
        width = i if not stack else i-1 - stack[-1][0]
        answer=max(answer,width*height)

    stack.append((i, cur_height))

while stack:
    idx, height = stack.pop()
    width = N if not stack else N-1 - stack[-1][0]
    answer=max(answer,width*height)

print(answer)
