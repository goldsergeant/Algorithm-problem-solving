N = int(input())
words = []
answer = 0
for _ in range(N):
    words.append(input())

words.sort(key=len)

for i in range(len(words)):
    flag=False
    for j in range(i+1,len(words)):
        if words[j].startswith(words[i]):
            flag=True
            break

    if not flag:
        answer+=1

print(answer)
