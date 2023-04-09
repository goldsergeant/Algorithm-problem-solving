import sys

n=int(input())
m=int(input())
break_buttons=[]
if m!=0:
    break_buttons=list(map(int,sys.stdin.readline().split()))
cur_channel=100
answer=abs(cur_channel-n)

for i in range(1000001):
    flag=0
    for break_button in break_buttons:
        if str(break_button) in str(i):
            flag=1
            break
    if flag==1:
        continue

    answer=min(answer,len(str(i))+abs(i-n))

print(answer)