def solution(n):
    answer=0
    for i in range(1,n//2+1):
        sum=0
        plus_number=i
        while sum<n:
            sum+=plus_number
            plus_number+=1
        if sum==n:
            answer+=1
    return answer+1