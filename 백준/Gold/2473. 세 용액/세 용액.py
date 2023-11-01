import sys
sys.setrecursionlimit(100000)

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
answer=[sys.maxsize,sys.maxsize,sys.maxsize]
arr.sort()
for i in range(n-2):
    left=i+1
    right=n-1

    while left<right:
        total=arr[i]+arr[left]+arr[right]
        if abs(sum(answer))>abs(total):
            answer=[arr[i],arr[left],arr[right]]

        if total<0:
            left+=1
        else:
            right-=1

print(*answer)
