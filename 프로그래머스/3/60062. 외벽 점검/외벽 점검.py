import collections
import itertools
import sys


def solution(n, weak, dist):
    answer = sys.maxsize
    for i in range(len(weak)):
        weak.append(weak[i] + n)

    for start_weak_idx in range(len(weak) // 2):
        test_weak = [weak[i] for i in range(start_weak_idx,start_weak_idx+len(weak)//2)]
        for dist_per in itertools.permutations(dist):
            dist_idx=0
            weak_idx=0
            pre_weak=test_weak[0]
            flag=False
            for _ in range(len(test_weak)):
                if flag or dist_idx==len(dist_per):
                    break
                while test_weak[weak_idx]<=pre_weak+dist_per[dist_idx]:
                    weak_idx+=1
                    if weak_idx==len(test_weak):
                        answer=min(answer,dist_idx+1)
                        flag=True
                        break
                else:
                    dist_idx+=1
                    pre_weak=test_weak[weak_idx]




    return answer if answer < sys.maxsize else -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
