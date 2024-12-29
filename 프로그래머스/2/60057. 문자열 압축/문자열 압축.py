import sys


def get_divisor(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)

    divisorsList.sort()

    return divisorsList


def solution(s):
    answer = len(s)
    divisor = get_divisor(len(s))
    divisor.pop()

    for cnt in range(1, len(s) // 2 + 1):
        cur = s[:cnt]
        temp_arr = []
        num = 1
        for i in range(cnt, len(s), cnt):
            if cur == s[i:i + cnt]:
                num += 1
            else:
                if num == 1:
                    temp_arr.append(cur)
                    cur = s[i:i + cnt]
                else:
                    temp_arr.append(f'{num}{cur}')
                    cur = s[i:i + cnt]
                    num = 1
        if num == 1:
            temp_arr.append(cur)
        else:
            temp_arr.append(f'{num}{cur}')

        # print(cnt)
        # print(''.join(temp_arr))
        answer = min(answer, len(''.join(temp_arr)))

    return answer

print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution('x'))