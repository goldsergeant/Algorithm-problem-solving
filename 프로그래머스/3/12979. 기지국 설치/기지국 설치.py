import math

def solution(n, stations, w):
    answer = 0
    stations=[-w]+stations+[n+1+w]
    
    not_located_cnts=[]
    for i in range(1,len(stations)):
        prev_end=stations[i-1]+w
        cur_start=stations[i]-w
        remain_section=cur_start-prev_end-1
        if remain_section>0:
            not_located_cnts.append(remain_section)
    
    cover_section=1+w*2
    for cnt in not_located_cnts:
        answer+=math.ceil(cnt/cover_section)
    
    print(not_located_cnts)
    return answer