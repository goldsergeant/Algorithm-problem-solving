import collections
import itertools
import sys

n,k=map(int,sys.stdin.readline().split())
know_words=dict()
know_words['a']=know_words['n']=know_words['t']=know_words['i']=know_words['c']=True
words=list(sys.stdin.readline().rstrip() for _ in range(n))
teach_words=set()
answer=0
if k<5:
    print(0)
    exit()

for word in words:
    for j in range(4,len(word)-4):
        if not know_words.get(word[j],False):
            teach_words.add(word[j])

if k-5>=len(teach_words):
    print(n)
    exit()

for teach in itertools.combinations(teach_words,k-5):
    tmp=0
    for word in teach:
        know_words[word]=True

    for word in words:
        flag=0
        for j in range(4,len(word)-4):
            if not know_words.get(word[j],False):
                flag=1
                break
        if flag==0:
            tmp+=1

    answer=max(answer,tmp)
    for word in teach:
        know_words[word]=False

print(answer)








