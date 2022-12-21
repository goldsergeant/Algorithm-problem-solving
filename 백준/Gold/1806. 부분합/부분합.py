import sys

n,s=map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
answer=sys.maxsize
left,right=0,0
cur_sum=0

while True:
    if cur_sum>=s:
        answer = min(answer, right - left)
        cur_sum -= arr[left]
        left+=1
    elif right==n:
        break
    elif cur_sum<s:
        cur_sum+=arr[right]
        right+=1

print(answer if answer!=sys.maxsize else 0)