def calc(times,limit_time):
    check=0
    for time in times:
        check+=limit_time//time

    return check
def solution(n, times):
    times.sort()
    left=times[0]
    right=times[0]*n

    while left+1<right:
        mid=(left+right)//2
        check=calc(times,mid)
        if check>=n:
            right=mid
        else:
            left=mid

    return right


print(solution(6, [7, 10]))
