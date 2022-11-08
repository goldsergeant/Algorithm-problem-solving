import collections
def solution(participant, completion):
    pCount=collections.Counter(participant)
    cCount=collections.Counter(completion)
    return ((pCount-cCount).most_common(1))[0][0]
    