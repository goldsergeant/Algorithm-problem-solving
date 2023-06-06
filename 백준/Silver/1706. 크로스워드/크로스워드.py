R, C = map(int, input().split())
puzzle = []
words = []
for _ in range(R):
    puzzle.append(input())

for i in range(R):  # 가로 단어 체크
    tmp = ''
    for j in range(C):
        if puzzle[i][j] == '#':
            if len(tmp) >= 2:
                words.append(tmp)
            tmp = ''
        else:
            tmp += puzzle[i][j]

        if j == C - 1 and len(tmp) >= 2:
            words.append(tmp)

for j in range(C): # 세로 단어 체크
    tmp=''
    for i in range(R):
        if puzzle[i][j] == '#':
            if len(tmp) >= 2:
                words.append(tmp)
            tmp = ''
        else:
            tmp += puzzle[i][j]

        if i == R - 1 and len(tmp) >= 2:
            words.append(tmp)

print(sorted(words)[0])