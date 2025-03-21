import sys

N = int(sys.stdin.readline())
competitions = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = dict()
dp[(0, 0)] = 0
dp[(0, 1)] = competitions[0][1]
for i in range(1, N):
    if dp.get((i - 1, i - 1), sys.maxsize) <= competitions[i][0]:
        dp[(i, i)] = min(dp.get((i - 1, i), sys.maxsize), dp[(i - 1, i - 1)] + competitions[i][1])
    else:
        dp[(i,i)]=dp.get((i-1,i),sys.maxsize)
    if dp.get((i - 1, i), sys.maxsize) <= competitions[i][0]:
        dp[(i, i + 1)] = min(dp.get((i - 1, i + 1), sys.maxsize), dp[(i - 1, i)] + competitions[i][1])
    else:
        dp[(i,i+1)]=dp.get((i - 1, i+1), sys.maxsize)

for i in range(N):
    if dp.get((i,N-1),sys.maxsize)<sys.maxsize or dp.get((i,N),sys.maxsize)<sys.maxsize:
        print('Kkeo-eok')
        exit()

print('Zzz')