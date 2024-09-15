import sys

N,T=map(int,sys.stdin.readline().split())
carrots=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

carrots.sort(key=lambda x:x[1]*T+x[0], reverse=True)

answer=0
for idx,carrot in enumerate(carrots):
    flavor,growth = carrot
    factor=T-idx-1
    answer+=flavor+growth*factor

print(answer)