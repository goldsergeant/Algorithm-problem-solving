import sys
from functools import cache

burger_length=[1 for _ in range(50 + 1)]
patty_length =[1 for _ in range(50+1)]
for i in range(1,50+1):
    burger_length[i]= 1 + burger_length[i - 1] + 1 + burger_length[i - 1] + 1
    patty_length[i]=patty_length[i-1]+1+patty_length[i-1]


N,X=map(int,sys.stdin.readline().split())

@cache
def dfs(n,x):
    if x==0:
        return 0
    if n==0:
        return 1
    if patty_length[n] < x:
        return patty_length[n-1]+1+dfs(n-1, x-patty_length[n]) # 중간 패티보다 많이 먹는 경우
    elif patty_length[n] == x:
        return patty_length[n-1]+1 # 중간 패티까지 먹는 경우
    else:
        return dfs(n - 1, x - 1); # 중간 패티보다 적게 먹는 경우


print(dfs(N,X))