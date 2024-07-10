import collections
import sys

def dfs(cur):
    if len(cur)==len(word):
        if cur not in existed:
            existed.add(cur)
            print(cur)
        return

    for key,val in counter.items():
        if val>0:
            counter[key]-=1
            dfs(cur+key)
            counter[key]+=1


N=int(sys.stdin.readline())
existed = set()

for _ in range(N):
    word=sorted(list(sys.stdin.readline().strip()))
    counter=collections.Counter(word)

    for i in range(len(word)):
        counter[word[i]]-=1
        dfs(word[i])
        counter[word[i]]+=1

