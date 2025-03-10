import collections
from itertools import combinations


def solution(orders, course):
    answer = []
    rank = [collections.defaultdict(int) for _ in range(10 + 1)]
    for order in orders:
        order = sorted(order)
        for cnt in course:
            for case in combinations(order, cnt):
                rank[cnt][tuple(case)] += 1

    for cnt in course:
        max_val = 2
        tmp = []
        for key, value in rank[cnt].items():
            if value > max_val:
                max_val = value
                tmp.clear()
                tmp.append(''.join(key))
            elif value == max_val:
                tmp.append(''.join(key))
        answer.extend(tmp)
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
