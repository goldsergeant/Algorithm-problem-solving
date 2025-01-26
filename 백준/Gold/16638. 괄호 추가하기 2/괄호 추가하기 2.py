import sys

N = int(sys.stdin.readline())
string = sys.stdin.readline().strip()
answer = -sys.maxsize


def dfs(idx, should_close, st):
    global answer
    if idx > N - 1:
        # print(st)
        answer = max(answer, eval(st))
        return
    if idx<N-1:
        opt = string[idx + 1]
        if should_close:
            dfs(idx + 2, False, f'{st}{string[idx]}){opt}')
        else:
            dfs(idx + 2, should_close, f'{st}{string[idx]}{opt}')
        if opt != '*' and not should_close:
            dfs(idx + 2, True, f'{st}({string[idx]}{opt}')

    else:
        if should_close:
            dfs(idx + 2, False, f'{st}{string[idx]})')
        else:
            dfs(idx+2,should_close,f'{st}{string[idx]}')

dfs(0, False, '')
print(answer)
