import collections
import sys

n,k=map(int,sys.stdin.readline().split())
students=list(sys.stdin.readline().rstrip() for _ in range(n))
dict=collections.defaultdict(int)
answer=0
right=0
for left in range(n):
    while right<n and right<left+k+1:
        answer+=dict[len(students[right])]
        dict[len(students[right])]+=1
        right+=1
    dict[len(students[left])]-=1


print(answer)