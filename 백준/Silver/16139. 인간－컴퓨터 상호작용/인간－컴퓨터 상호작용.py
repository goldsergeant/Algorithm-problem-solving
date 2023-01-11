import sys

s=input()
q=int(input())
for _ in range(q):
    a,l,r=sys.stdin.readline().split()
    l,r=int(l),int(r)
    print(s[l:r+1].count(a))