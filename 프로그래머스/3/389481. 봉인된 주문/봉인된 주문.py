def get_origin_num_of_word(word):
    num = 0

    for i in range(len(word)):
        n = ord(word[i]) - ord('a')
        num = num * 26 + n+1
    return num


def get_word_from_num(num):
    tmp = []
    while num > 0:
        num-=1
        tmp.append(chr(97+(num%26)))
        num //= 26

    return ''.join(tmp[::-1])


def solution(n, bans):
    for i in range(len(bans)):
        bans[i] = get_origin_num_of_word(bans[i])

    bans.sort()
    for i in range(len(bans)):
        if bans[i] <= n:
            n += 1

    return get_word_from_num(n)


print(solution(30, ["d", "e", "bb", "aa", "ae"]))
print(solution(7388, ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]))
# print(get_origin_num_of_word('aa'))