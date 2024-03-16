import sys

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
answer=0

for i in range(N):
    if numbers[i]==0:
        continue
    answer+=1
    tmp=numbers[i]
    numbers[i]=0
    for j in range(i+1,N):
        if tmp-1==numbers[j]:
            tmp-=1
            numbers[j]=0

print(answer)