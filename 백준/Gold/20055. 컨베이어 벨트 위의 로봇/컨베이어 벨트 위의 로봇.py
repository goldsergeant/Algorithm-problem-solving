import collections
import sys

N, K = map(int, sys.stdin.readline().split())
up_idx, down_idx = 0, N - 1
belt = collections.deque(list(map(int, sys.stdin.readline().split())))
there_robot = collections.deque([0 for _ in range(N)])
zero_cnt = 0
answer = 0


def up_robot():
    global zero_cnt
    if belt[up_idx] > 0:
        there_robot[up_idx] += 1
        belt[up_idx] -= 1
        if belt[up_idx] == 0:
            zero_cnt += 1


def rotate():
    belt.rotate(1)
    there_robot.rotate(1)


def move_robots():
    global zero_cnt
    idx = len(there_robot) - 1
    while idx >= 0:
        while there_robot[idx] > 0:
            if there_robot[idx + 1] == 0 and belt[idx + 1] > 0:
                there_robot[idx], there_robot[idx + 1] = there_robot[idx] - 1, 1
                belt[idx + 1] -= 1
                if belt[idx + 1] == 0:
                    zero_cnt += 1
                down_robot()
            else:
                break
        idx -= 1


def down_robot():
    there_robot[down_idx] = 0


while zero_cnt < K:
    answer += 1
    down_robot()
    rotate()
    down_robot()
    move_robots()
    down_robot()
    up_robot()
print(answer)
