import collections
import itertools
import sys


def compute_cnt(weak,dist):
    dist_idx = 0
    weak_idx = 0
    pre_weak = weak[0]
    for _ in range(len(weak)):
        while weak[weak_idx] <= pre_weak + dist[dist_idx]:
            weak_idx += 1
            if weak_idx == len(weak):
                return dist_idx+1
        else:
            dist_idx += 1
            if dist_idx== len(dist):
                return sys.maxsize
            pre_weak = weak[weak_idx]
def solution(n, weak, dist):
    answer = sys.maxsize
    for i in range(len(weak)):
        weak.append(weak[i] + n)

    for start_weak_idx in range(len(weak) // 2):
        test_weak = [weak[i] for i in range(start_weak_idx,start_weak_idx+len(weak)//2)]
        for dist_per in itertools.permutations(dist):
            answer=min(answer,compute_cnt(test_weak,dist_per))

    return answer if answer < sys.maxsize else -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
