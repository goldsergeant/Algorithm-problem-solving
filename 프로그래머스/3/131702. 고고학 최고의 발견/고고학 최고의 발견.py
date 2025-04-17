import copy
import itertools
import sys

TOP=0
RIGHT=1
BOTTOM=2
LEFT=3


def solution(clockHands):
    def make_top_cases(depth):
        if depth==len(clockHands):
            top_cases.append(cur_top[::])
            return

        for n in range(4):
            cur_top.append(n)
            make_top_cases(depth+1)
            cur_top.pop()

    def rotate(clock_hands,r, c,cnt):
        clock_hands[r][c]=(clock_hands[r][c]+cnt)%4
        for dr, dc in (0, -1), (0, 1), (1, 0), (-1, 0),:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(clock_hands) and 0 <= nc < len(clock_hands):
                clock_hands[nr][nc] = (clock_hands[nr][nc]+cnt)%4

    answer = sys.maxsize
    cur_top=[]
    top_cases=[]
    make_top_cases(0)
    for top_case in top_cases:
        tmp_clock=copy.deepcopy(clockHands)
        tmp_cnt=0
        for j in range(len(top_case)):
            rotate(tmp_clock,0,j,top_case[j])
            tmp_cnt+=top_case[j]

        for i in range(1,len(clockHands)):
            for j in range(len(clockHands)):
                cnt= (4-tmp_clock[i-1][j])%4
                rotate(tmp_clock,i,j,cnt)
                tmp_cnt+=cnt

        if all(i==TOP for i in tmp_clock[-1]):
            answer=min(answer,tmp_cnt)

    return answer

