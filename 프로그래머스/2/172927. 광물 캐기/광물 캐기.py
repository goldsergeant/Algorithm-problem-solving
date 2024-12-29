import sys

def solution(picks, minerals):
    global answer
    def get_cost(start_idx,pick):
        cost=0
        for i in range(start_idx,min(start_idx+5,len(minerals))):
            if minerals[i]=='diamond':
                if pick=='diamond':
                    cost+=1
                elif pick=='iron':
                    cost+=5
                else:
                    cost+=25
            elif minerals[i]=='iron':
                if pick=='stone':
                    cost+=5
                else:
                    cost+=1
            else:
                cost+=1
        return cost
                    
    def dfs(idx,dia,iron,stone,total):
        global answer
        if idx>=len(minerals) or (dia,iron,stone)==(0,0,0):
            answer=min(answer,total)
            return
        
        if dia>0:
            dfs(idx+5,dia-1,iron,stone,total+get_cost(idx,'diamond'))
        if iron>0:
            dfs(idx+5,dia,iron-1,stone,total+get_cost(idx,'iron'))
        if stone>0:
            dfs(idx+5,dia,iron,stone-1,total+get_cost(idx,'stone'))
                    
                
    answer = sys.maxsize
    dfs(0,picks[0],picks[1],picks[2],0)
    return answer