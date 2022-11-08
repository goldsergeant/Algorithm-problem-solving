def solution(board, moves):
    result=0
    dolls=[]
    for move in moves:
        for i in board:
            if i[move-1]!=0:
                dolls.append(i[move-1])
                while len(dolls)>1 and dolls[-1]==dolls[-2]:
                    result+=2
                    dolls.pop(-1)
                    dolls.pop(-1)
                i[move-1]=0
                break
    return result