import sys

N,M=map(int,sys.stdin.readline().split())
answer=sys.maxsize
arr=list(int(sys.stdin.readline()) for _ in range(N))
arr.sort()

right=1
for left in range(N-1):
    while True:
        if arr[right]-arr[left]>=M or right==N-1:
            break
        right+=1

    if arr[right]-arr[left]>=M:
        answer=min(answer,arr[right]-arr[left])


print(answer)
