import sys
from heapq import heappush, heappop


def solution(target):
    answer = []
    visited = [[sys.maxsize, -sys.maxsize] for _ in range(target + 1)]
    visited[0] = [0, 0]
    heap = [(0, 0, 0)]

    while heap:
        cnt, single_or_bull, num = heappop(heap)
        single_or_bull = -single_or_bull

        if cnt > visited[num][0] or (cnt == visited[num][0] and single_or_bull < visited[num][1]):
            continue

        if num == target:
            return [cnt, single_or_bull]

        for i in range(1, 20 + 1):
            for factor in range(1, 3 + 1):
                n_num = num + i * factor
                if n_num > target:
                    continue
                if factor==1:
                    if cnt + 1 < visited[n_num][0] or (
                            cnt + 1 == visited[n_num][0] and single_or_bull+1 > visited[n_num][1]):
                        visited[n_num] = [cnt + 1, single_or_bull+1]
                        heappush(heap, (cnt + 1, -(single_or_bull+1), n_num))
                else:
                    if cnt + 1 < visited[n_num][0] or (cnt + 1 == visited[n_num][0] and single_or_bull > visited[n_num][1]):
                        visited[n_num] = [cnt + 1, single_or_bull]
                        heappush(heap, (cnt + 1, -single_or_bull, n_num))

        n_num = num + 50
        if n_num > target:
            continue
        if cnt + 1 < visited[n_num][0] or (cnt + 1 == visited[n_num][0] and single_or_bull + 1 > visited[n_num][1]):
            visited[n_num] = [cnt + 1, single_or_bull + 1]
            heappush(heap, (cnt + 1, -(single_or_bull+1), n_num))

    return answer

print(solution(21))
print(solution(58))