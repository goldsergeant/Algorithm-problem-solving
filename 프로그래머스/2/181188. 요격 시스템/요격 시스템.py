def solution(targets):
    answer=0
    targets.sort(key=lambda x:(x[1],x[0]))
    
    cur_end=0
    for s,e in targets:
        if cur_end<=s:
            answer+=1
            cur_end=e              
  
    return answer