ATTACK = 1
HEALING = 2

def solution(board, skill):
    answer = 0
    imos=[[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for type,r1,c1,r2,c2,how_many in skill:
        if type==ATTACK:
            imos[r1][c1]-=how_many
            imos[r2+1][c2+1]-=how_many

            imos[r1][c2+1]+=how_many
            imos[r2+1][c1]+=how_many
        else:
            imos[r1][c1]+=how_many
            imos[r2+1][c2+1]+=how_many

            imos[r1][c2+1]-=how_many
            imos[r2+1][c1]-=how_many

    for i in range(len(imos)):
        for j in range(1,len(imos[0])):
            imos[i][j]+=imos[i][j-1]

    for i in range(1,len(imos)):
        for j in range(len(imos[0])):
            imos[i][j]+=imos[i-1][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]+imos[i][j]>0:
                answer+=1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))

print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))