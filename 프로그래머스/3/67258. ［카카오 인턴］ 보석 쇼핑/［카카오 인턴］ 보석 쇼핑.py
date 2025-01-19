import collections
import sys


def solution(gems):
    answer = [0,sys.maxsize]

    target_length = len(set(gems))
    counter=collections.Counter()
    right=0
    for left in range(len(gems)):
        while right<len(gems) and len(counter)<target_length:
            counter[gems[right]]+=1
            right+=1

        if len(counter)==target_length and (right-1)-left<answer[1]-answer[0]:
            answer=[left,right-1]

        counter[gems[left]]-=1
        if counter[gems[left]]==0:
            counter.pop(gems[left])

    return list(map(lambda x:x+1,answer))