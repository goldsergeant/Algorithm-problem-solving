import sys

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.insert(0,0)
    rocks.append(distance)

    def check(val):
        chance=n
        if val==2:
            pass
        prev=0
        for i in range(1,len(rocks)):
            if rocks[i]-rocks[prev]<val:
                if chance>0:
                    chance-=1
                    continue
                else:
                    return False
            prev=i

        return True

    left=1
    right=1000000000

    while left+1<right:
        mid=(left+right)//2
        if check(mid):
            left=mid
        else:
            right=mid
    return left

