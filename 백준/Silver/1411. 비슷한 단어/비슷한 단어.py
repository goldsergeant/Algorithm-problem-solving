N = int(input())
words = []
answer = 0
for _ in range(N):
    words.append(input())

for i in range(N):
    for j in range(i + 1, N):
        tmp1 = words[i]
        tmp2 = words[j]

        dic1 = dict()
        dic2 = dict()
        is_similar = True
        for k in range(len(words[i])):
            if dic1.get(tmp1[k], '*') == '*' and dic2.get(tmp2[k],'*')=='*':
                dic1[tmp1[k]] = tmp2[k]
                dic2[tmp2[k]]= tmp1[k]
            elif dic1.get(tmp1[k],'*') != tmp2[k]:
                is_similar = False
                break
        if is_similar:
            answer+=1

print(answer)
