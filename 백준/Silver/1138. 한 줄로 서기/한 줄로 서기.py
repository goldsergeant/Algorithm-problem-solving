import itertools
import sys

N=int(sys.stdin.readline())
how_many_left=list(map(int,sys.stdin.readline().split()))

def check(case):
    for i in range(len(case)):
        cnt=0
        for j in range(i-1,-1,-1):
            if case[j]>case[i]:
                cnt+=1
        if cnt!=how_many_left[case[i]-1]:
            return False
    return True


for case in itertools.permutations([i for i in range(1,N+1)],N):
    if check(case):
        print(*case)
        exit()