import sys

sys.setrecursionlimit(10000)


def solution(commands):
    def find(r, c):
        if parent[r][c] != (r, c):
            parent[r][c] = find(parent[r][c][0], parent[r][c][1])

        return parent[r][c]

    def union(r1, c1, r2, c2):
        # parent[r2][c2]=(r1,c1)
        parent[r2][c2]=r1,c1

    board = [['' for _ in range(50 + 1)] for _ in range(50 + 1)]
    parent = [[(i, j) for j in range(50 + 1)] for i in range(50 + 1)]
    answer = []

    for command in commands:
        args = command.split()
        query = args[0]
        if query == 'UPDATE':
            if len(args) == 4:  # update r c value
                r, c, value = args[1:]
                r, c = find(int(r), int(c))
                board[r][c] = value
            elif len(args) == 3:  # update value1 value2
                value1, value2 = args[1:]
                for i in range(1, 50 + 1):
                    for j in range(1, 50 + 1):
                        i, j = find(i, j)
                        if board[i][j] == value1:
                            board[i][j] = value2

        elif query == 'MERGE':
            r1, c1, r2, c2 = map(int, args[1:])
            r1, c1 = find(r1, c1)
            r2, c2 = find(r2, c2)
            if (r1, c1) == (r2, c2):
                continue
            val = board[r1][c1] or board[r2][c2]
            union(r1, c1, r2, c2)
            r, c = find(r1, c1)
            board[r][c] = val

        elif query == 'UNMERGE':
            r, c = map(int, args[1:])
            origin_r, origin_c = r, c
            r, c = find(r, c)
            pre_value = board[r][c]
            unmerge_list = []
            for i in range(1, 50 + 1):
                for j in range(1, 50 + 1):
                    if find(i, j) == (r, c):
                        unmerge_list.append((i, j))

            for i, j in unmerge_list:
                parent[i][j] = (i, j)
                board[i][j] = ''
            board[origin_r][origin_c] = pre_value
        elif query == 'PRINT':
            r, c = map(int, args[1:])
            r, c = find(r, c)
            answer.append(board[r][c] if board[r][c] != '' else 'EMPTY')

    return answer


# print(solution(
#     ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 3 3",
#      "UNMERGE 1 1", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))
print(solution(
    ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4",
     "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))
# print(solution(["MERGE 1 1 2 2", "PRINT 1 1"]))
# print(solution(["MERGE 1 1 2 2",
#                 "UPDATE 1 1 A",
#                 "UNMERGE 1 1",
#                 "PRINT 1 1",
#                 "PRINT 2 2"]))
# print(
#     solution(
#         ["UPDATE 1 1 menu", "MERGE 1 1 1 2", "MERGE 1 1 1 3", "MERGE 1 1 1 4", "MERGE 1 2 1 3", "UPDATE 1 1 hansik",
#          "PRINT 1 1", "PRINT 1 2", "PRINT 1 3", "PRINT 1 4"]
#         ))
