import sys

N,M,K=map(int,sys.stdin.readline().split())
answer=0
for i in range(K+1):
    remove_n=i
    remove_m=K-remove_n

    temp_N=N-remove_n
    temp_M=M-remove_m
    count=0
    while temp_N>1 and temp_M>0:
        count+=1
        temp_N-=2
        temp_M-=1
    answer=max(answer,count)

print(answer)