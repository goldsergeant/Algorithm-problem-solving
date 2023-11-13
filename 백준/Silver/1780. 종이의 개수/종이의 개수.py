import collections
import sys

n = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = collections.defaultdict(int)


def divide(s_r, s_c, size):
    if size==1:
        answer[papers[s_r][s_c]]+=1
        return
    is_all_same = True
    for i in range(s_r, s_r + size):
        for j in range(s_c, s_c + size):
            if papers[i][j] != papers[s_r][s_c]:
                is_all_same = False
                break

    if is_all_same:
        answer[papers[s_r][s_c]] += 1
        return

    for i in range(s_r,s_r+size,size//3):
        for j in range(s_c,s_c+size,size//3):
            divide(i,j,size//3)

divide(0,0,n)

for i in [-1,0,1]:
    print(answer[i])