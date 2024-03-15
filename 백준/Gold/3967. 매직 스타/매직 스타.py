import sys

magic_star = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
x_positions = []
visited=[False for _ in range(12+1)]
answer = []


def get_num_of_alphbet(alphabet):
    return ord(alphabet) - 64


def check():
    if sum(get_num_of_alphbet(magic_star[y][x]) for y, x in [(0, 4), (1, 3), (2, 2), (3, 1)]) != 26:
        return False
    if sum(get_num_of_alphbet(magic_star[y][x]) for y, x in [(0, 4), (1, 5), (2, 6), (3, 7)]) != 26:
        return False
    if sum(get_num_of_alphbet(magic_star[y][x]) for y, x in [(1, 1), (1, 3), (1, 5), (1, 7)]) != 26:
        return False
    if sum(get_num_of_alphbet(magic_star[y][x]) for y, x in [(3, 1), (3, 3), (3, 5), (3, 7)]) != 26:
        return False
    if sum(get_num_of_alphbet(magic_star[y][x]) for y, x in [(1, 1), (2, 2), (3, 3), (4, 4)]) != 26:
        return False
    if sum(get_num_of_alphbet(magic_star[y][x]) for y, x in [(1, 7), (2, 6), (3, 5), (4, 4)]) != 26:
        return False

    return True


for i in range(5):
    for j in range(9):
        if magic_star[i][j] == 'x':
            x_positions.append((i, j))
        elif magic_star[i][j]!='.':
            num=get_num_of_alphbet(magic_star[i][j])
            visited[num]=True


def dfs(idx):
    if idx == len(x_positions):
        if check():
            print('\n'.join(''.join(sub_arr) for sub_arr in magic_star))
            exit()
        return

    for i in range(1,12+1):
        if not visited[i]:
            visited[i]=True
            y,x=x_positions[idx]
            magic_star[y][x]=chr(i+64)
            dfs(idx+1)
            magic_star[y][x]='x'
            visited[i]=False

dfs(0)
