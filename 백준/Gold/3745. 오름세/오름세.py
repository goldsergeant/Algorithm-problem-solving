import sys
from bisect import bisect_left,bisect_right

while True:
    try:
        N=int(sys.stdin.readline())
        numbers=list(map(int,sys.stdin.readline().split()))
        arr=[numbers[0]]
        for num in numbers[1:]:
            if arr[-1]<num:
                arr.append(num)
            else:
                idx=bisect_left(arr,num)
                arr[idx]=num

        print(len(arr))
    except ValueError:
        break