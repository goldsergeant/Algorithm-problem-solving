import sys

e,s,m=map(int,sys.stdin.readline().split())
year=1
e1,s1,m1=1,1,1
while True:
    if e1==e and s1==s and m1==m:
        print(year)
        break
    e1=e1+1
    if e1==16:
        e1=1
    s1=s1+1
    if s1==29:
        s1=1
    m1=m1+1
    if m1==20:
        m1=1

    year+=1