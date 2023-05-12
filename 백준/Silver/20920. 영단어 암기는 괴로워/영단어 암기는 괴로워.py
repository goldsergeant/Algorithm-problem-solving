import collections
import sys

N,M=map(int,sys.stdin.readline().split())
words=dict()
for _ in range(N):
    word=sys.stdin.readline().strip()
    if len(word)>=M:
        if words.get(word,0)==0:
            words[word]=1
        else:
            words[word]+=1

counter=collections.Counter(words)
answer=sorted(words.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in answer:
    print(i[0])