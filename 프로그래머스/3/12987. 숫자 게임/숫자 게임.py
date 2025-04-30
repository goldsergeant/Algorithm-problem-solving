from bisect import bisect_right,bisect_left
def solution(A, B):
    answer = 0
    B.sort()
    
    for n in A:
        idx=bisect_right(B,n)
        if idx<len(B):
            answer+=1
            B.pop(idx)
    return answer