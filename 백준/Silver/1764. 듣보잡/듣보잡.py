import sys

n,m=map(int,sys.stdin.readline().split())
listen=set()
see=set()
for i in range(n):
    listen.add(input())
for i in range(m):
    see.add(input())

print(len(listen.intersection(see)))
for i in sorted(listen.intersection(see)):
    print(i)