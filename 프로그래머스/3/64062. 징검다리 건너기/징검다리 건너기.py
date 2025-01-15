def solution(stones, k):
    def check(num) -> bool:
        num-=1
        cnt = 0
        for stone in stones:
            if stone - num <= 0:
                cnt += 1
                if cnt == k:
                    return False
            else:
                cnt = 0

        return True

    left = 1
    right = max(stones)+1

    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid

    return left


# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([5],5))