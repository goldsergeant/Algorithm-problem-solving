import collections
import sys
sys.setrecursionlimit(100000)

n,m=map(int,sys.stdin.readline().split())
lamps=[]
answer=0

def get_zero_cnt(idx):
    return sum(i==0 for i in lamps[idx])

for _ in range(n):
    lamps.append(list(map(int,sys.stdin.readline().rstrip())))

k=int(sys.stdin.readline())

for i in range(n):
    zero_cnt=get_zero_cnt(i)
    if zero_cnt<=k and zero_cnt%2==k%2:
        tmp=1
        for j in range(i+1,n):
            if lamps[i]==lamps[j]:
                tmp+=1
        answer=max(answer,tmp)

print(answer)