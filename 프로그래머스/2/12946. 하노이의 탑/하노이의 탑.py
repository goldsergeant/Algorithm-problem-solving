def solution(n):
    answer = []
    
    def hanoi(num,a_tower,b_tower):
        if num==1:
            answer.append([a_tower,b_tower])
            return
        
        c_tower=6-a_tower-b_tower
        hanoi(num-1,a_tower,c_tower)
        answer.append([a_tower,b_tower])
        hanoi(num-1,c_tower,b_tower)
    
    hanoi(n,1,3)
    return answer