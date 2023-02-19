def solution(clothes):

    answer=1
    dic=dict()
    for clothe, type in clothes:
        dic[type] = dic.get(type, 0) + 1

    for type in dic:
        answer*=(1+dic[type])


    return answer-1