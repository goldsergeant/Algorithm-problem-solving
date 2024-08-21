import sys

st=sys.stdin.readline().rstrip()
left_k,right_k=[],[]

cnt=0
for ch in st:
    if ch=='K':
        cnt+=1
    else:
        left_k.append(cnt)

cnt=0
for ch in st[::-1]:
    if ch=='K':
        cnt+=1
    else:
        right_k.append(cnt)

right_k.reverse()

left=0
right=len(left_k)-1
answer=0

while left<=right:
    answer=max(answer, right-left+1+2*(min(left_k[left],right_k[right])))
    if left_k[left]<right_k[right]:
        left+=1
    else:
        right-=1

print(answer)