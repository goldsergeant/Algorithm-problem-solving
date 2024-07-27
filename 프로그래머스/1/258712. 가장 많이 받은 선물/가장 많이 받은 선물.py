import collections
import itertools

def solution(friends, gifts):
    answer = 0
    graph=collections.defaultdict(int)
    gift_score_dict=collections.defaultdict(int)
    gift_cnt=collections.defaultdict(int)
    for st in gifts:
        giver,receiver=st.split()
        graph[(giver,receiver)]+=1
        gift_score_dict[giver]+=1
        gift_score_dict[receiver]-=1
        
    for a,b in itertools.combinations(friends,2):
        if graph[(a,b)]> graph[(b,a)]:
            gift_cnt[a]+=1
        elif graph[(a,b)]< graph[(b,a)]:
            gift_cnt[b]+=1
        else:
            if gift_score_dict[a]>gift_score_dict[b]:
                gift_cnt[a]+=1
            elif gift_score_dict[a]<gift_score_dict[b]:
                gift_cnt[b]+=1
    print(gift_cnt)
    for key,value in gift_cnt.items():
        answer=max(answer,value)
    return answer