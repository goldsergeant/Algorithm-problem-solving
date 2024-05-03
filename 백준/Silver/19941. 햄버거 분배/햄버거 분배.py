import sys

N,K=map(int,sys.stdin.readline().split())
st=list(sys.stdin.readline().rstrip())
answer=0
for i in range(len(st)):
    if st[i]=='P':
        for j in range(i-K,i+K+1):
            if 0<=j<N:
                if st[j]=='H':
                    answer+=1
                    st[j]='-'
                    break

print(answer)