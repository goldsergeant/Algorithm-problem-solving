import sys

N=int(sys.stdin.readline())
A,B,C,D=[],[],[],[]
for _ in range(N):
    a,b,c,d=map(int,sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab=[]
cd=[]
answer=0

for i in range(N):
    for j in range(N):
        ab.append(A[i]+B[j])
        cd.append(C[i]+D[j])

ab.sort()
cd.sort()

left=0
right=len(cd)-1

while left<len(ab) and right>=0:
    if ab[left]+cd[right]==0:
        next_left,next_right=left+1,right-1
        while next_left<len(ab) and ab[left]==ab[next_left]:
            next_left+=1
        while next_right>=0 and cd[right]==cd[next_right]:
            next_right-=1

        answer+=(next_left-left)*(right-next_right)
        left=next_left
        right=next_right

    elif ab[left]+cd[right]<0:
        left+=1
    else:
        right-=1

print(answer)