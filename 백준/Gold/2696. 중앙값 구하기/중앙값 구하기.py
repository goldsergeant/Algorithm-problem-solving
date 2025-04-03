import sys
import math
from bisect import bisect_left

T=int(sys.stdin.readline())
for _ in range(T):
    M=int(sys.stdin.readline())
    numbers=[]
    for _ in range(math.ceil(M/10)):
        numbers.extend(list(map(int,sys.stdin.readline().split())))

    arr=[]
    answer=[]

    for i,num in enumerate(numbers):
        if not arr or arr[-1]<=num:
            arr.append(num)
        else:
            idx=bisect_left(arr,num)
            arr.insert(idx,num)

        if i%2==0:
            answer.append(arr[len(arr)//2])

    print(len(answer))
    for i in range(len(answer)):
        print(answer[i],end=' ')
        if (i+1)%10==0 and i<len(answer)-1:
            print()
    print()