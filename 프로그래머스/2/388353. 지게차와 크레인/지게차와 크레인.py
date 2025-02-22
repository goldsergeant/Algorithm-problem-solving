import collections


def remove_outside(storage, target):
    have_to_remove = []
    visited=[[False for _ in range(len(storage[0]))] for _ in range(len(storage))]
    q=collections.deque([(0,0)])
    visited[0][0]=True

    while q:
        r,c=q.popleft()
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc=r+dy,c+dx
            if 0<=nr<len(storage) and 0<=nc<len(storage[0]):
                if visited[nr][nc]:
                    continue
                visited[nr][nc]=True
                if storage[nr][nc]=='.':
                    q.append((nr,nc))
                elif storage[nr][nc]==target:
                    have_to_remove.append((nr,nc))


    for i,j in have_to_remove:
        storage[i][j]='.'

def remove_all_target(storage, target):
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] == target:
                storage[i][j] = '.'


def solution(storage, requests):
    answer = 0
    storage = [list('.' * (len(storage[0]) + 2))] + storage + [list('.' * (len(storage[0]) + 2))]
    for i in range(1, len(storage) - 1):
        storage[i] = ['.'] + list(storage[i]) + ['.']

    for query in requests:
        if len(query) == 1:
            target = query[0]
            remove_outside(storage, target)
        else:
            target = query[0]
            remove_all_target(storage, target)

        # for arr in storage:
        #     print(arr)
        # print()

    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] != '.':
                answer += 1


    return answer


print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))
