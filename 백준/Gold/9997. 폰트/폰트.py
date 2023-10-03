import collections
import sys

n=int(sys.stdin.readline())
words=[0 for _ in range(n)]
for i in range(n):
    word=sys.stdin.readline().rstrip()
    for char in word:
        words[i] |= 1<<ord(char)-97
answer=0
is_alphabet=(1<<26)-1

def dfs(depth,mask):
    global answer
    if depth==n:
        if mask==is_alphabet:
            answer+=1
        return

    dfs(depth+1,mask|words[depth])
    dfs(depth+1,mask)

dfs(0,0)

print(answer)

