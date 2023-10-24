import sys

n = int(sys.stdin.readline())
buildings = list(map(int, sys.stdin.readline().split()))
see_buildings = [0] * (n)
near_buildings = [sys.maxsize] * (n)

stack = []
for idx, height in enumerate(buildings):
    while stack and buildings[stack[-1]] <= height:
        stack.pop()
    see_buildings[idx] += len(stack)

    if stack:
        near_buildings[idx] = min(near_buildings[idx], stack[-1], key=lambda x: (abs(idx - x), x))

    stack.append(idx)

stack = []
for i in reversed(range(n)):
    while stack and buildings[stack[-1]] <=buildings[i]:
        stack.pop()
    see_buildings[i]+=len(stack)

    if stack:
        near_buildings[i]=min(near_buildings[i],stack[-1],key=lambda x:(abs(i-x),x))

    stack.append(i)

for i in range(n):
    if see_buildings[i]>0:
        print(see_buildings[i],near_buildings[i]+1)
    else:
        print(0)
