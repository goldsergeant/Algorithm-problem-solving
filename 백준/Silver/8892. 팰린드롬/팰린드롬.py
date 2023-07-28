import sys

t=int(input())
for _ in range(t):
    k=int(input())
    words=[]
    for _ in range(k):
        words.append(sys.stdin.readline().rstrip())
    answer=[]

    for i in range(k):
        for j in range(k):
            if i!=j:
                merged_word=words[i]+words[j]
                if merged_word==merged_word[::-1]:
                    answer.append(merged_word)

    if answer:
        print(answer[0])
    else:
        print(0)

