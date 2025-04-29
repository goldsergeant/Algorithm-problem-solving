def solution(bandage, health, attacks):
    answer = 0
    cur_health=health
    cur_time=1
    cur_seq_cnt=0
    
    for time,damage in attacks:
        while cur_time<time:
            cur_seq_cnt+=1
            if cur_seq_cnt==bandage[0]:
                cur_health=min(health,cur_health+bandage[1]+bandage[2])
                cur_seq_cnt=0
            else:
                cur_health=min(health,cur_health+bandage[1])
            print(f'cur_time : {cur_time}, cur_health : {cur_health}, seq_cnt : {cur_seq_cnt}')
            cur_time+=1
        cur_health-=damage
        cur_seq_cnt=0
        cur_time+=1
        if cur_health<=0:
            return -1
            
    return cur_health