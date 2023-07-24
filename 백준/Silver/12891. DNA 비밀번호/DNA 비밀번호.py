import collections
import sys

s,p=map(int,sys.stdin.readline().split())
dna=sys.stdin.readline()
a,c,g,t=map(int,sys.stdin.readline().split())
answer=0

left=0
right=p-1
counter=collections.Counter(dna[left:right+1])
while right<s:
    if counter['A']>=a and counter['C']>=c and counter['G']>=g and counter['T']>=t:
        answer+=1

    counter[dna[left]]-=1
    left+=1
    right+=1
    counter[dna[right]]+=1

print(answer)