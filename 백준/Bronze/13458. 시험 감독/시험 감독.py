import math

N=int(input())
arr=list(map(int,input().split()))
B,C=map(int,input().split())
answer=0

for i in range(len(arr)):
    arr[i]-=B
    answer+=1
    if arr[i]>0:
        answer+=math.ceil(arr[i]/C)

print(answer)