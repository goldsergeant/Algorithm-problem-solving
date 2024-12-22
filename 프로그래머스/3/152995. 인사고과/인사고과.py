def solution(scores):
    rank=1
    wanho_score=scores[0]
    
    scores.sort(key=lambda x:(-x[0],x[1]))
    max_b=0
    
    for a,b in scores:
        if max_b<=b:
            max_b=b
            if a+b>sum(wanho_score):
                rank+=1
        else:
            if [a,b]==wanho_score:
                return -1
    
    return rank