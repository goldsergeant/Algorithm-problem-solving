import sys

n=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
sort_chance=int(sys.stdin.readline())

for i in range(len(numbers)-1):
    if sort_chance==0:
        break
    max_idx=i+1
    for j in range(i+1,min(i+1+sort_chance,len(numbers))):
        if numbers[max_idx]<numbers[j]:
            max_idx=j
    if numbers[max_idx]>numbers[i]:
        numbers.insert(i,numbers.pop(max_idx))
        sort_chance-=max_idx-i
print(*numbers)