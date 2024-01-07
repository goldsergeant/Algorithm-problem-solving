import itertools
import sys

N=int(sys.stdin.readline())
numbers=[int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()
for i in range(N-1,-1,-1):
    for j in range(i):
        target = numbers[i]-numbers[j]
        left,right=j,i
        while left<=right:
            total=numbers[left]+numbers[right]
            if total<target:
                left+=1
            elif total>target:
                right-=1
            else:
                print(numbers[i])
                exit()

