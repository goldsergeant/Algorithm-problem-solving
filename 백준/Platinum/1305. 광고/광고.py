import sys


def failure(pattern):
    table=[0]*len(pattern)
    i=0
    for j in range(1,len(pattern)):
        while i>0 and pattern[i]!=pattern[j]:
            i=table[i-1]
        if pattern[i]==pattern[j]:
            i+=1
            table[j]=i
    return table[-1]

l=int(sys.stdin.readline().rstrip())
st=sys.stdin.readline().rstrip()
print(l-failure(st))