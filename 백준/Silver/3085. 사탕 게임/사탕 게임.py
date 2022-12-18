import collections

n = int(input())
arr = collections.deque()
for _ in range(n):
    arr.append(list(input()))
result = []


def check():
    num = 1
    for i in range(n):
        for j in range(1,n):
            if arr[i][j-1]==arr[i][j]:
                num+=1
            elif arr[i][j-1]!=arr[i][j]:
                num=1
            if num not in result:
                result.append(num)
        num=1
        for j in range(1,n):
            if arr[j-1][i]==arr[j][i]:
                num+=1
            elif arr[j-1][i]!=arr[j][i]:
                num=1
            if num not in result:
                result.append(num)
        num=1

for i in range(n):
    for j in range(n):
        if j > 0 and arr[i][j-1]!=arr[i][j]:
            arr[i][j - 1], arr[i][j] = arr[i][j], arr[i][j - 1]
            check()
            arr[i][j - 1], arr[i][j] = arr[i][j], arr[i][j - 1]
        if j < n - 1 and arr[i][j+1]!=arr[i][j]:
            arr[i][j + 1], arr[i][j] = arr[i][j], arr[i][j + 1]
            check()
            arr[i][j + 1], arr[i][j] = arr[i][j], arr[i][j + 1]
        if i < n - 1 and arr[i+1][j]!=arr[i][j]:
            arr[i + 1][j], arr[i][j] = arr[i][j], arr[i + 1][j]
            check()
            arr[i + 1][j], arr[i][j] = arr[i][j], arr[i + 1][j]
        if i > 0 and arr[i-1][j]!=arr[i][j]:
            arr[i - 1][j], arr[i][j] = arr[i][j], arr[i - 1][j]
            check()
            arr[i - 1][j], arr[i][j] = arr[i][j], arr[i - 1][j]
check()
print(max(result) if len(result)>0 else n)