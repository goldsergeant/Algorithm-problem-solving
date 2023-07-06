import sys

r, c = map(int, input().split())
words = []
answer = []
for _ in range(r):
    words.append(sys.stdin.readline().rstrip())

for i in range(r):
    tmp = ''
    for j in range(c):
        if words[i][j] == '#':
            if len(tmp) >= 2:
                answer.append(tmp)
            tmp=''
            continue
        tmp += words[i][j]
    if len(tmp) >= 2:
        answer.append(tmp)

for i in range(c):
    tmp = ''
    for j in range(r):
        if words[j][i] == '#':
            if len(tmp)>=2:
                answer.append(tmp)
            tmp=''
            continue
        tmp += words[j][i]

    if len(tmp) >= 2:
        answer.append(tmp)

print(sorted(answer)[0])
