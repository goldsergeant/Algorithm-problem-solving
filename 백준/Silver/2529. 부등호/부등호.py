import sys

k = int(input())
signs = list(sys.stdin.readline().split())
visited = [False for _ in range(10)]
answer = []


def check(sign, a, b) -> bool:
    if sign == '<':
        return a < b
    else:
        return a > b


def dfs(numbers):
    if len(numbers) == k + 1:
        answer.append(numbers)
        return

    for i in range(10):
        if not visited[i] and check(signs[len(numbers)-1],int(numbers[-1]),int(i)):
            visited[i] = True
            dfs(numbers + str(i))
            visited[i] = False


for i in range(10):
    visited[i] = True
    dfs(str(i))
    visited[i] = False

print(answer[-1])
print(answer[0])
