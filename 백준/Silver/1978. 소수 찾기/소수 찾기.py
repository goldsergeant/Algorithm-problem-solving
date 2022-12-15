import sys

n=int(input())
answer=0
numArr=map(int,input().split())
for num in numArr:
    flag=0
    if num==1:
        continue
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    if flag==0:
        answer+=1
print(answer)