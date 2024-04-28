import sys

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
numbers.sort()
if N%2==0:
    print(numbers[len(numbers)//2-1])
else:
    print(numbers[len(numbers)//2])

