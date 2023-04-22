import sys #백트래킹으로 풀기

n, m = map(int, sys.stdin.readline().split())
arr = []
answer = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))
check = [[False for _ in range(m)] for _ in range(n)]


def dfs(i, j):
    if i==n:
        answer.append(calc())
        return

    if j==m:
        dfs(i+1,0)
        return

    check[i][j]=True
    dfs(i,j+1)
    check[i][j]=False
    dfs(i,j+1)


def calc() -> int:
    total = 0
    for row in range(n):
        row_sum = 0
        for col in range(m):  # 가로 연산 체크되어있으면 쭉
            if check[row][col]:
                row_sum = row_sum * 10 + arr[row][col]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    for col in range(m):
        col_sum = 0
        for row in range(n):
            if not check[row][col]:
                col_sum = col_sum * 10 + arr[row][col]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
    return total

dfs(0,0)
print(max(answer))