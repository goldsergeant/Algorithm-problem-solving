import collections
import sys

n = int(input())
like_students = dict()
seats = [[0 for _ in range(n)] for _ in range(n)]
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def calc_score(num):  # 만족하는 첫번째 인덱스 넘기기
    tmp_score = []
    for row in range(n):
        for col in range(n):
            if seats[row][col] == 0:  # 빈자리인 경우
                like = 0
                empty = 0
                for i in range(4):
                    ny = row + dy[i]
                    nx = col + dx[i]
                    if ny < 0 or nx < 0 or ny > n - 1 or nx > n - 1:
                        continue
                    if seats[ny][nx] == 0:
                        empty += 1
                    elif seats[ny][nx] in like_students[num]:
                        like += 1
                tmp_score.append([like, empty, row, col])

    tmp_score.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]), reverse=True)
    first_point = (tmp_score[0][2], tmp_score[0][3])
    return first_point

def calc_satisfaction():
    score = 0
    for row in range(n):
        for col in range(n):
            satis=0
            for i in range(4):
                ny = row + dy[i]
                nx = col + dx[i]
                if ny < 0 or nx < 0 or ny > n - 1 or nx > n - 1:
                    continue
                if seats[ny][nx] in like_students[seats[row][col]]:
                    satis+=1
            score+=10**satis//10
    return score


for _ in range(n * n):
    numbers = list(map(int, sys.stdin.readline().split()))
    like_students[numbers[0]] = numbers[1:]

for key in like_students.keys():
    row,col=calc_score(key)
    seats[row][col]=key

print(calc_satisfaction())