import sys


def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

n=int(input())
buildings=list(map(int,input().split()))
answer=[]
for i in range(n):
    left_see_count=0
    left=i-1
    min_slope=sys.maxsize
    while left>=0:
        if min_slope>slope(i,buildings[i],left,buildings[left]):
            left_see_count+=1
            min_slope=slope(i,buildings[i],left,buildings[left])
        left-=1

    right=i+1
    max_slope=-sys.maxsize
    right_see_count=0
    while right < n:
        if max_slope < slope(i, buildings[i], right,buildings[right]):
            max_slope = slope(i, buildings[i], right,buildings[right])
            right_see_count+=1
        right+=1

    answer.append(left_see_count+right_see_count)

print(max(answer))