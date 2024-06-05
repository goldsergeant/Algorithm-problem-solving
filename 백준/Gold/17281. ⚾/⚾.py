import sys
from itertools import permutations

ANTA = 1
ROOTA_2 = 2
ROOTA_3 = 3
HOME_RUN = 4
OUT = 0


N = int(sys.stdin.readline())
inings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
roota1,roota2,roota3=False,False,False
for p in permutations([i for i in range(1, 9)], 8):
    p = list(p)
    order = p[:3] + [0] + p[3:]
    score = 0
    idx = 0
    for i in range(N):
        out = 0
        roota1,roota2,roota3=False,False,False
        while out < 3:
            state = inings[i][order[idx]]
            if state == OUT:
                out += 1
            elif state == ANTA:
                score += roota3
                roota1,roota2,roota3=True,roota1,roota2
            elif state == ROOTA_2:
                score += roota2+roota3
                roota1,roota2,roota3=False,True,roota1
            elif state == ROOTA_3:
                score += roota1+roota2+roota3
                roota1,roota2,roota3=False,False,True
            elif state == HOME_RUN:
                if roota1:
                    score+=1
                if roota2:
                    score+=1
                if roota3:
                    score+=1
                score+=1
                roota1, roota2, roota3 = False, False, False
            idx = (idx + 1) % 9
    answer = max(answer, score)
print(answer)
