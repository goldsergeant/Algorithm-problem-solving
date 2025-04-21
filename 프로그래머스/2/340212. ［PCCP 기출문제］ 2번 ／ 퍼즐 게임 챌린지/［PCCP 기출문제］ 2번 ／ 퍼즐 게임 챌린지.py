def solution(diffs, times, limit):
    def check(level):
        cost=0
        for i in range(len(diffs)):
            if level<diffs[i]:
                cnt=diffs[i]-level
                time_prev=times[i-1]
                cost+=(time_prev+times[i])*cnt+times[i]
            else:
                cost+=times[i]
        return cost<=limit
    
    answer = 0
    left=0
    right=10**15
    
    while left+1<right:
        mid=(left+right)//2
        if not check(mid):
            left=mid
        else:
            right=mid
    return right