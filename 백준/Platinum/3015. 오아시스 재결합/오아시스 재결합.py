import collections
import sys

n = int(input())
heights = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
answer = 0

for idx,cur_people in enumerate(heights):
    while stack and stack[-1][0]<cur_people:
        answer+=stack.pop()[1]

    if not stack:
        stack.append([cur_people,1])
        continue

    if stack[-1][0]==cur_people:
        tmp=stack.pop()[1]
        answer+=tmp
        if stack:
            answer+=1
        stack.append([cur_people,tmp+1])

    elif stack[-1][0]>cur_people:
        stack.append([cur_people,1])
        answer+=1


print(answer)
