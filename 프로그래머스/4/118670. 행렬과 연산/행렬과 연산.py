import collections


def solution(rc, operations):
    answer = []
    rows=collections.deque([collections.deque(rc[i][1:-1]) for i in range(len(rc))])
    left_col = collections.deque([rc[i][0] for i in range(len(rc))])
    right_col = collections.deque([rc[i][-1] for i in range(len(rc))])

    def rotate():
        left_top=left_col.popleft()
        rows[0].appendleft(left_top)

        right_top=rows[0].pop()
        right_col.appendleft(right_top)

        right_bottom=right_col.pop()
        rows[-1].append(right_bottom)

        left_bottom=rows[-1].popleft()
        left_col.append(left_bottom)

    def shift_row():
        rows.rotate(1)
        left_col.rotate(1)
        right_col.rotate(1)

    for op in operations:
        if op=='Rotate':
            rotate()
        else:
            shift_row()

    for i in range(len(rows)):
        answer.append([left_col.popleft()]+list(rows[i])+[right_col.popleft()])

    return answer

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],	["Rotate", "ShiftRow"]))