import collections
def solution(N, stages):
    answer = []
    challenge=len(stages)
    count=collections.Counter(stages)
    for i in range(1,N+1):
        if challenge<=0:
            answer.append((0,-i))
        else:
            answer.append((count[i]/challenge,-i))
            challenge-=count[i]
    answer.sort(reverse=True,key=lambda x:(x[0],x[1]))
    return [-i[1] for i in answer]