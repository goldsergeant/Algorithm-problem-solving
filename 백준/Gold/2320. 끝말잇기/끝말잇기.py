import sys


def dfs(last_word, words_bit):
    if dp[last_word][words_bit] != -1:
        return dp[last_word][words_bit]

    dp[last_word][words_bit] = len(words[last_word])

    for i in range(N):
        if words_bit & (1 << i):
            continue
        if words[last_word][-1] == words[i][0]:
            dp[last_word][words_bit] = max(dp[last_word][words_bit],
                                           len(words[last_word]) + dfs(i, words_bit | (1 << i)))

    return dp[last_word][words_bit]


N = int(sys.stdin.readline())
words = [list(sys.stdin.readline().strip()) for _ in range(N)]
dp = [[-1 for _ in range(1 << N)] for _ in range(N)]  # 마지막 단어, 거쳤던 단어
answer = 0
for i in range(N):
    answer = max(answer, dfs(i, 1 << i))

print(answer)
