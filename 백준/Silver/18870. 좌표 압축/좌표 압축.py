import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
orderArr=[]
order=0
tempArr=sorted(arr)
dict=dict()
dict[tempArr[0]]=order
answer=[]
for i in range(1,len(tempArr)):
    if tempArr[i]>tempArr[i-1]:
        order+=1
    dict[tempArr[i]]=order

for i in range(len(arr)):
    answer.append(dict[arr[i]])
print(*answer)