import sys

N = int(input())
dx = [-1, 0, 1]
a = list(map(int, sys.stdin.readline().strip()))
b = list(map(int, sys.stdin.readline().strip()))

def check(temp):
    for i in range(N):
        if temp[i] != b[i]:
            return False
    return True


def change(temp, idx):
    for i in range(3):
        nx = idx + dx[i]
        if nx < 0 or nx > N - 1:
            continue
        temp[nx] = 1 - temp[nx]


def go(version):
    temp = a.copy()
    count = 0

    if version == 0:
        change(temp,0)
        count+=1
        for i in range(1,N):
            if temp[i-1] != b[i-1]:
                change(temp, i)
                count += 1

    elif version == 1:
        for i in range(1, N):
            if temp[i - 1] != b[i - 1]:
                change(temp, i)
                count += 1

    return count if check(temp) else sys.maxsize


answer = min(go(0), go(1))
print(answer if answer != sys.maxsize else -1)
