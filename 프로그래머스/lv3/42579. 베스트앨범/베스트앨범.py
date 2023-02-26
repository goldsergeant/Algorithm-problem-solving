import collections
def solution(genres, plays):
    answer = []
    dic=collections.defaultdict(list)
    orderlist=[]
    for i in range(len(genres)):
        dic[genres[i]].append((plays[i],i))
    
    for i in dic.keys():
        dic[i].sort(key=lambda x:(x[0],-x[1]),reverse=True)
        
    for i in sorted(dic.keys(),key=lambda x:(sum([i[0] for i in dic[x]])),reverse=True):
        orderlist.append(i)
    
    for order in orderlist:
        count=0
        for i in dic[order]:
            if count<2:
                answer.append(i[1])
                count+=1
    
    return answer