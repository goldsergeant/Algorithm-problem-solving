import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
check_list = [[0 for _ in range(m)] for _ in range(n)]
answer = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))


def check_sum():
    for i in range(1 << (n * m)):
        total = 0

        for row in range(n):
            row_sum = 0
            for col in range(m):
                idx = row * m + col
                if i & (1 << idx) == 0:  # 가로 연산
                    row_sum = row_sum * 10 + arr[row][col]
                else:
                    total += row_sum
                    row_sum = 0
            total += row_sum

        for col in range(m):
            col_sum = 0
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) != 0: #세로 연산
                    col_sum = col_sum * 10 + arr[row][col]
                else:
                    total += col_sum
                    col_sum = 0
            total += col_sum
        answer.append(total)


check_sum()

print(max(answer))
