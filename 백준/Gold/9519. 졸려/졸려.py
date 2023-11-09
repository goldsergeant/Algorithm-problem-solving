import sys

x = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()
changed_words = [word]


def change(st: str):
    cnt = len(st) // 2
    stack = []
    for i in range(len(st)):
        if i % 2 == 1:
            stack.append(st[i])
        if len(stack) == cnt:
            break

    tmp=''.join([st[i] for i in range(0,len(st),2)])
    while stack:
        tmp+=stack.pop()

    return tmp


idx = 0
while True:
    idx += 1
    word=change(word)

    if idx==x:
        print(word)
        exit()

    if word in changed_words:
        print(''.join(changed_words[x%len(changed_words)]))
        exit()

    else:
        changed_words.append(word)

