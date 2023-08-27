import sys

n=int(input())
alphabets=[[0,False] for _ in range(10)] # 0부터 A,B,C ~
answer=0

for _ in range(n):
    word=sys.stdin.readline().rstrip()
    plus=1
    alphabets[ord(word[0])-65][1]=True
    for i in range(len(word)-1,-1,-1):
        alphabets[ord(word[i])-65][0]+=plus
        plus*=10

alphabets.sort(reverse=True)
if alphabets[9][0]!=0:
    for i in range(len(alphabets)-1,-1,-1):
        if not alphabets[i][1]:
            alphabets.pop(i)
            break

for i in range(len(alphabets)):
    answer+=alphabets[i][0]*(9-i)

print(answer)