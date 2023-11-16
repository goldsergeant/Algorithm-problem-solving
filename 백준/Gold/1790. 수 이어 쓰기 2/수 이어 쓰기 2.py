import sys

n,k=map(int,sys.stdin.readline().split())

digit=1
num_cnt=9
step_last_num=0

while k>digit*num_cnt:
    step_last_num+=num_cnt
    k-= digit * num_cnt
    digit+=1
    num_cnt*=10

answer_num= (step_last_num+1) + (k-1) // digit

if answer_num>n:
    print(-1)
else:
    answer_num_str=str(answer_num)
    print(answer_num_str[(k-1) % digit])
