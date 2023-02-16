import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
tempArr=sorted(list(set(arr)))
dic={tempArr[i]:i for i in range(len(tempArr))}

for i in arr:
    print(dic[i], end= ' ')