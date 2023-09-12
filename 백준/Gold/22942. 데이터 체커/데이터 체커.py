import sys

n=int(input())
circles=[]
for i in range(n):
    x,r=map(int,sys.stdin.readline().split())
    circles.append((x-r,i))
    circles.append((x+r,i))
circles.sort()
stack=[]
for i in range(len(circles)):
    if not stack:
        stack.append(circles[i])
        continue
    stack.pop() if stack[-1][1]==circles[i][1] else stack.append(circles[i])

print('YES' if not stack else 'NO')