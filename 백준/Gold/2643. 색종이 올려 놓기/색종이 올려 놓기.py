import sys
from functools import cache


@cache
def dfs(idx,w,h):
    tmp = 1

    for i in range(len(papers)):
        if i == idx:
            continue

        width, height = papers[i]

        if w >= width and h >= height:
            tmp = max(tmp, 1 + dfs(i,width, height))

        if w >= height and h >= width:
            tmp = max(tmp, 1 + dfs(i,height, width))

    return tmp


N = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 1
for i in range(len(papers)):
    w,h=papers[i]
    # print(f'w,h : {w},{h}, dfs : {dfs(w,h)}')
    answer = max(answer, dfs(i,w, h))

print(answer)
