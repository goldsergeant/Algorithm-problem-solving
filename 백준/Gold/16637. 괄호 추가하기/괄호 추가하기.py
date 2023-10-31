import sys

n=int(sys.stdin.readline())
exp=sys.stdin.readline().rstrip()
answer=[]


def dfs(idx,total):
    if idx==n-1:
        answer.append(total)
        return

    dfs(idx+2,eval(f'{total}{exp[idx+1]}{exp[idx+2]}'))

    if idx<=n-4:
        dfs(idx+4,eval(f'{total}{exp[idx+1]}{eval(exp[idx+2:idx+5])}'))


dfs(0,exp[0])

print(max(answer))