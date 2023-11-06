import sys

n=int(sys.stdin.readline())
weight_limits=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
boxes=list(map(int,sys.stdin.readline().split()))
answer=0

weight_limits.sort(reverse=True)
boxes.sort(reverse=True)

if max(weight_limits)<max(boxes):
    print(-1)
    exit()

while boxes:
    answer+=1
    for i in range(n):
        for j in range(len(boxes)):
            if weight_limits[i]>=boxes[j]:
                del boxes[j]
                break

print(answer)
