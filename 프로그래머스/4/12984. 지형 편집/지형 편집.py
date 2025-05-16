import sys
import collections

def solution(land, P, Q):
    answer = sys.maxsize
    
    land=[j for i in land for j in i]
    land.sort()
    left=0
    right=sum(land)
    for i in range(len(land)):
        target=land[i]
        right-=target
        left_diff=i*target-left
        right_diff=right-(len(land)-i-1)*target
        left+=target
        
        answer=min(answer,left_diff*P+right_diff*Q)
        
                
    return answer