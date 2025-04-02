import sys

direction = [(), (-1, 0), (1, 0), (0, 1), (0, -1)]
sharks = dict()
R, C, M = map(int, sys.stdin.readline().split())
answer=0
def catch_shark(fisher_c):
    for r in range(1,R+1):
        if (r,fisher_c) in sharks:
            return sharks.pop((r,fisher_c))[2]

    return 0
def move_sharks():
    global sharks
    new_sharks = dict()
    for r, c in sharks.keys():
        s, d, z = sharks[(r, c)]
        remain_move_cnt=s
        new_r, new_c = r, c
        while remain_move_cnt > 0:
            prev_r,prev_c=new_r,new_c
            new_r, new_c = new_r + direction[d][0] * remain_move_cnt, new_c + direction[d][1] * remain_move_cnt

            if new_r < 1 or new_c < 1 or new_r > R or new_c > C:
                if new_r > R:
                    new_r = R
                elif new_r < 1:
                    new_r = 1
                elif new_c > C:
                    new_c = C
                elif new_c < 1:
                    new_c = 1

                remain_move_cnt -= abs(prev_r-new_r) or abs(prev_c-new_c)
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                elif d == 4:
                    d = 3

            else:
                remain_move_cnt = 0

        if (new_r,new_c) in new_sharks:
            if z>new_sharks[(new_r,new_c)][2]:
                new_sharks[(new_r,new_c)] = (s,d,z)
        else:
            new_sharks[(new_r,new_c)] = (s,d,z)
    sharks=new_sharks



for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())  # s 속력, d는 방향,
    sharks[(r, c)] = (s, d, z)

for fisher_c in range(1, C + 1):
    answer+=catch_shark(fisher_c)
    move_sharks()
print(answer)