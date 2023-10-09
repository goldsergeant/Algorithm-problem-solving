import sys


def create_table(pattern):
    table = [0] * len(pattern)

    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    return table


def kmp(all_string, pattern):
    table = create_table(pattern)

    i = 0
    result = []
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i - 1]

        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                result.append(j - i + 2)
                i=table[i-1]

    return result


all_string = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()

answer=kmp(all_string,pattern)
print(len(answer))
print(*answer)
