import sys

n,m=map(int,sys.stdin.readline().split())
set1=set()
set2=[]
for i in range(n):
    set1.add(input())

for i in range(m):
    set2.append(input())

length=0
for node in set2:
    if node in set1:
        length+=1
print(length)