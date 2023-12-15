import sys


while True:
    heights=list(map(int,sys.stdin.readline().split()))[1:]
    answer=0
    if not heights:
        break
    stack=[]
    for i in range(len(heights)):
        if not stack:
            stack.append(i)
            continue

        while stack and heights[stack[-1]]>heights[i]:
            removed_idx=stack.pop()
            height=heights[removed_idx]
            width =i if not stack else i-1-stack[-1]
            answer=max(answer,width*height)

        stack.append(i)

    while stack:
        removed_idx = stack.pop()
        height=heights[removed_idx]
        width = len(heights) if not stack else len(heights)-1-stack[-1]
        answer = max(answer, width * heights[removed_idx])

    print(answer)