def solution(n):
    
    def hanoi(num,a_tower,b_tower):
        if num==1:
            yield [a_tower,b_tower]
            return
        
        c_tower=6-a_tower-b_tower
        yield from hanoi(num-1,a_tower,c_tower)
        yield [a_tower,b_tower]
        yield from hanoi(num-1,c_tower,b_tower)
    
    return list(hanoi(n,1,3))
    