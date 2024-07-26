def solution(users, emoticons):
    answer = []
    discount_rate=[10,20,30,40]
    cases=[]
    
    def dfs(idx,case):
        if idx==len(emoticons):
            cases.append(case)
            return
        
        for i in range(4):
            dfs(idx+1,case+[discount_rate[i]])
    
    dfs(0,[])
    
    for case in cases:
        total_cost,plus_service_cnt=0,0

        for i in range(len(users)):
            cost=0
            possible_rate,plus_service_cost=users[i]
            
            for idx,emoticon_price in enumerate(emoticons):
                case_discount_rate=case[idx]
                if case_discount_rate>=possible_rate:
                    cost+=emoticon_price*((100-case_discount_rate)/100)
            
            if cost>=plus_service_cost:
                plus_service_cnt+=1
            else:
                total_cost+=cost
                
        answer.append((plus_service_cnt,total_cost))
                
                
            
    return sorted(answer,key=lambda x:(x[0],x[1]),reverse=True)[0]