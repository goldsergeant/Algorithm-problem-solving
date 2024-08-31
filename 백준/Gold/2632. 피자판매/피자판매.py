import sys
from collections import defaultdict

target_size=int(sys.stdin.readline())
N,M=map(int,sys.stdin.readline().split())
A=list(int(sys.stdin.readline()) for _ in range(N))
B=list(int(sys.stdin.readline()) for _ in range(M))
a_dict=defaultdict(int)
b_dict=defaultdict(int)
answer=0
for i in range(N):
    tmp=0
    for j in range(i,i+N-1):
        tmp+=A[j%N]
        a_dict[tmp]+=1

a_dict[sum(A)]=1
a_dict[0]=1

for i in range(M):
    tmp=0
    for j in range(i,i+M-1):
        tmp+=B[j%M]
        b_dict[tmp]+=1
b_dict[sum(B)]=1
b_dict[0]=1
for key,value in a_dict.items():
    answer+=value*b_dict[target_size-key]

print(answer)