import sys

t=int(sys.stdin.readline())
for _ in range(t):
    b,d=sys.stdin.readline().split()
    b=int(b)

    num=sum(map(int,list(d)))
    print(num%(b-1))
