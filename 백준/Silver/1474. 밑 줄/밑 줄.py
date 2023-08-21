import sys

n,m=map(int,sys.stdin.readline().split())
words=[sys.stdin.readline().rstrip() for _ in range(n)]
fill_length,short_word=divmod(m-sum(map(len,words)),n-1)

answer=words[0]

for i in range(1,n):
    if words[i][0].islower() and short_word>0:
        short_word-=1
        answer+='_'*(fill_length+1)+words[i]
    elif n==i+short_word and short_word>0:
        short_word-=1
        answer+='_'*(fill_length+1)+words[i]
    else:
        answer+='_'*fill_length+words[i]

print(answer)