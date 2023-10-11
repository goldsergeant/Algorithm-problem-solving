import collections
import sys

n=int(sys.stdin.readline())
score=collections.defaultdict(int)
words=[]
answer=0

for _ in range(n):
    word=sys.stdin.readline().rstrip()
    for i in range(len(word)):
        score[word[i]]+=10**(len(word)-i-1)
    words.append(word)

sorted_alphabet=sorted(score.keys(),key=lambda x:score[x],reverse=True)
for i in range(len(sorted_alphabet)):
    score[sorted_alphabet[i]]=9-i

for i in range(len(words)):
    for j in range(len(words[i])):
        answer+=10**(len(words[i])-j-1)*score[words[i][j]]

print(answer)
