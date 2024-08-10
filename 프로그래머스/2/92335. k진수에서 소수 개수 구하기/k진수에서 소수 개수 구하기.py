import math


def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n, k):
    cache = dict()

    def is_prime(num):
        if num in cache.keys():
            return cache[num]

        if num <= 1:
            cache[num] = False
            return False

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                cache[num] = False
                return False

        cache[num] = True
        return True

    answer = 0
    n = convert(n, k)
    numbers = []
    for val in list(n.split('0')):
        if val.isdigit():
            numbers.append(int(val))

    for num in numbers:
        if is_prime(num):
            answer += 1

    return answer

