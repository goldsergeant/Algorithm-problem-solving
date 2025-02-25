import collections
import itertools
from bisect import bisect_left


def solution(info, query):
    answer = []
    dict = collections.defaultdict(list)
    for string in info:
        lang, job, career, soul_food, score = string.split()
        score = int(score)
        dict[(lang, job, career, soul_food)].append(score)
        for cnt in range(1, 4 + 1):
            for case in itertools.combinations([i for i in range(1, 4 + 1)], cnt):
                arr = [lang, job, career, soul_food]
                for idx in case:
                    arr[idx - 1] = '-'
                dict[tuple(arr)].append(score)

    for key in dict.keys():
        dict[key].sort()

    for string in query:
        string = string.replace('and', ' ', string.count('and'))
        lang, job, career, soul_food, score = string.split()
        score = int(score)
        arr = dict[(lang, job, career, soul_food)]
        cnt = len(arr) - bisect_left(arr, score)
        answer.append(cnt)

    return answer