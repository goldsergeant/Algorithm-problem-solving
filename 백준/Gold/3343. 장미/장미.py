import sys
import math

N, A, B, C, D = map(int, sys.stdin.readline().split())
mini_cnt, mini_price, maxi_cnt, maxi_price = 0, 0, 0, 0
answer = sys.maxsize
if A * D > C * B:
    mini_cnt, mini_price = C, D
    maxi_cnt, maxi_price = A, B
else:
    mini_cnt, mini_price = A, B
    maxi_cnt, maxi_price = C, D

for i in range(maxi_cnt):
    cnt = math.ceil((N - i * mini_cnt) / maxi_cnt)
    is_over = False
    if cnt < 0:
        cnt = 0
        is_over = True
    answer = min(answer, i * mini_price + cnt * maxi_price)
    if is_over:
        break

print(answer)
