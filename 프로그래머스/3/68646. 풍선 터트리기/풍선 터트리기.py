import sys

def solution(a):
    answer = len(a)
    left=[0 for _ in range(len(a))]
    right=[0 for _ in range(len(a))]
    
    tmp=sys.maxsize
    for i in range(len(a)):
        tmp=min(tmp,a[i])
        left[i]=tmp
    
    tmp=sys.maxsize
    
    for i in range(len(a)-1,-1,-1):
        tmp=min(tmp,a[i])
        right[i]=tmp
    
    for i in range(1,len(a)-1):
        if left[i-1]<a[i] and right[i+1]<a[i]:
            answer-=1
            
    return answer