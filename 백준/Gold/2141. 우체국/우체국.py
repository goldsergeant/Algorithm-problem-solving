import sys

n=int(input())
village=[]
sum_people=0

for _ in range(n):
    num1,num2=map(int,sys.stdin.readline().split())
    village.append((num1,num2))
    sum_people+=num2

village.sort()

cur_people=0
for i in range(n):
    cur_people+=village[i][1]
    if cur_people>=sum_people/2:
        print(village[i][0])
        break


