import sys

t = int(sys.stdin.readline())


def dfs(num, limit, exp, answer):
    if num == limit:
        if ' ' in exp:
            if eval(exp.replace(' ',''))==0:
                answer.append(exp)
        else:
            if eval(exp)==0:
                answer.append(exp)
        return

    dfs(num + 1, limit, f'{exp}+{num + 1}', answer)
    dfs(num + 1, limit, f'{exp}-{num + 1}', answer)
    dfs(num + 1, limit, f'{exp} {num + 1}', answer)


for _ in range(t):
    n = int(sys.stdin.readline())
    answer = []
    dfs(1, n, '1', answer)
    answer.sort()
    for st in answer:
        print(st)
    print()