def solution(sequence, k):
    answer = []
    
    right=0
    cur_sum=0
    for left in range(len(sequence)):
        while cur_sum<k and right<len(sequence):
            cur_sum+=sequence[right]
            right+=1
        
        if cur_sum==k:
            answer.append([left,right-1])
        
        cur_sum-=sequence[left]
                            
    
    answer.sort(key=lambda x:((x[1]-x[0]),x[0],x[1]))
    return answer[0]