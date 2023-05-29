import collections
import sys

M,N=map(int,sys.stdin.readline().split())

dic=dict()
dic['0']= "zero"
dic['1']= "one"
dic['2']= "two"
dic['3']= "three"
dic['4']= "four"
dic['5']= "five"
dic['6']= "six"
dic['7']= "seven"
dic['8']= "eight"
dic['9']= "nine"

dic2=collections.defaultdict(str)

arr=[]
for i in range(M,N+1):
    arr.append(str(i))

for num in arr:
    for j in range(len(num)):
        dic2[num]+=dic[num[j]]

arr.sort(key=lambda x:dic2[x])

idx=0
while True:
    if idx==len(arr):
        break

    print(arr[idx],end=' ')
    idx+=1
    if idx%10==0:
        print()
