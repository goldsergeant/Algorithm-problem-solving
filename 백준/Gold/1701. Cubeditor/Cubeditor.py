import sys

st=sys.stdin.readline().rstrip()
answer=0

def get_max(pattern:str)->int:
    i=0
    table=[0]*len(pattern)
    max_num=0
    for j in range(1, len(pattern)):
        while i>0 and pattern[i]!=pattern[j]:
            i=table[i-1]

        if pattern[i]==pattern[j]:
            i+=1
            table[j]=i
            max_num=max(max_num,table[j])
    return max_num


for i in range(len(st)):
    answer=max(answer,get_max(st[i:]))

print(answer)