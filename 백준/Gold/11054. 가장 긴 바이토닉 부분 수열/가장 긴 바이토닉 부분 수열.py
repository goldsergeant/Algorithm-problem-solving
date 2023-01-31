import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
answer=0
increase=[1 for i in range(n)]
decrease=[1 for i in range(n)]
for i in range(1,n):
    for j in range(0,i+1):
        if arr[j]<arr[i]:
            increase[i]=max(increase[i],increase[j]+1)

for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        if arr[j]>arr[i]:
            decrease[j]=max(decrease[j],decrease[i]+1)

for i in range(n):
    answer=max(answer,increase[i]+decrease[i]-1)

print(answer)