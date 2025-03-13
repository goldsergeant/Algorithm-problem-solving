import math

def solution(players, m, k):
    answer = 0
    servers=[0 for _ in range(len(players))]
    
    for i in range(len(players)):
        if players[i]//m>servers[i]:
            increment=players[i]//m-servers[i]
            answer+=increment
            for j in range(i,min(i+k,len(players))):
                servers[j]+=increment
    print(servers)
    return answer