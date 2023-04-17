import itertools
import sys

while True:
    numbers=list(map(int,sys.stdin.readline().split()))
    k=numbers[0]

    if k==0:
        break

    s=numbers[1:]

    combi=itertools.combinations(s,6)
    for i in combi:
        print(*i)
    print()