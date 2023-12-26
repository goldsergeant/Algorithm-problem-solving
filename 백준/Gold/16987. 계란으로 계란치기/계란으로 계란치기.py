import sys


def my_input():
    return sys.stdin.readline().rstrip()


N = int(my_input())
eggs = []
answer = 0
for _ in range(N):
    s, w = map(int, my_input().split())
    eggs.append([s, w])


def smash_eggs(i, j):
    eggs[i][0] -= eggs[j][1]
    eggs[j][0] -= eggs[i][1]


def recover_eggs(i, j):
    eggs[i][0] += eggs[j][1]
    eggs[j][0] += eggs[i][1]


def dfs(left):
    global answer
    if left == N:
        answer = max(answer, len(list(filter(lambda x: x[0] <= 0, eggs))))
        return

    if eggs[left][0]>0:
        is_all_broken=True
        for i in range(N):
            if i!=left and eggs[i][0]>0:
                is_all_broken=False
                smash_eggs(left,i)
                dfs(left+1)
                recover_eggs(left,i)
        if is_all_broken:
            dfs(N)
    else:
        dfs(left+1)


dfs(0)
print(answer)
