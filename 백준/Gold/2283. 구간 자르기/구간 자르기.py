import sys

N,K=map(int,sys.stdin.readline().split())
min_left,max_right=sys.maxsize,0
MAX_NUM=1000000
contain_lines=[0]*(MAX_NUM+2)
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    for i in range(a+1,b+1):
        contain_lines[i]+=1

left,right,total=0,0,0
while left<MAX_NUM+1 and right < MAX_NUM+1:
    if total<K:
        right+=1
        total+=contain_lines[right]
    elif total>K:
        left+=1
        total-=contain_lines[left]
    else:
        print(left,right)
        exit()

print(0,0)
