import itertools


def solution(numbers):
    answer=[]
    def is_prime(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    arr = []
    for i in range(1, len(numbers) + 1):
        arr += itertools.permutations(numbers, i)
    arr = list(map(''.join, arr))
    for i in arr:
        if is_prime(int(i)):
            answer.append(int(i))
    return len(set(answer))