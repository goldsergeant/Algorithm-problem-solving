from itertools import combinations


def solution(n, q, ans):
    def check(case):
        for i in range(len(q)):
            tmp = 0
            for j in range(len(q[i])):
                if q[i][j] in case:
                    tmp += 1

            if tmp != ans[i]:
                return False
        return True

    answer = 0
    cnt = 0
    for case in combinations([i for i in range(1, n + 1)], 5):
        if check(case):
            cnt += 1

    return cnt

print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))