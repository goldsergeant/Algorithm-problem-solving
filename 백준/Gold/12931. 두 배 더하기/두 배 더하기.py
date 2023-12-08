import sys

N=int(sys.stdin.readline())
a_arr=[0]*N
b_arr=list(map(int,sys.stdin.readline().split()))
total_zero_cnt=b_arr.count(0)
answer=0

while total_zero_cnt<N:
    for i in range(N):
        if b_arr[i]%2==1:
            answer+=1
            b_arr[i]-=1
            if b_arr[i]==0:
                total_zero_cnt+=1

    if total_zero_cnt<N:
        b_arr=[i//2 for i in b_arr]
        answer+=1

print(answer)