def solution(nums):
    answer=len(nums)//2
    kind=len(set(nums))
    return min(answer,kind)
        
    
            