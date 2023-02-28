import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))

house_count = []
global house_cnt
house_cnt=0


def dfs(i, j, number, depth):
    global house_cnt
    arr[i][j] = number
    if i > 0 and arr[i - 1][j] == '1':
        house_cnt+=1
        dfs(i - 1, j, number, depth + 1)
    if j > 0 and arr[i][j - 1] == '1':
        house_cnt+=1
        dfs(i, j - 1, number, depth + 1)
    if i < n - 1 and arr[i + 1][j] == '1':
        house_cnt+=1
        dfs(i + 1, j, number, depth + 1)
    if j < n - 1 and arr[i][j + 1] == '1':
        house_cnt+=1
        dfs(i, j + 1, number, depth + 1)

count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            count += 1
            house_cnt=1
            dfs(i, j, count, 1)
            house_count.append(house_cnt)
print(count)
for num in sorted(house_count):
    print(num)
