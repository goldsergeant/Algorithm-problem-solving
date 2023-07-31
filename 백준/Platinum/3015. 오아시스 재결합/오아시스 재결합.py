import collections
import sys

n = int(input())
heights = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
answer = 0

for cur_people in heights:
    while stack and stack[-1][0]<cur_people:
        answer+=stack.pop()[1]

    if not stack:
        stack.append([cur_people,1])
        continue

    if stack[-1][0]>cur_people:
        answer+=1
        stack.append([cur_people,1])

    elif stack[-1][0]==cur_people:
        tmp=stack.pop()[1]
        answer+=tmp
        if stack:
            answer+=1
        stack.append([cur_people,tmp+1])


print(answer)
