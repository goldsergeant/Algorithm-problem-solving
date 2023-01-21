n=int(input())
board=[0]*n
answer=0

def checkBoard(i):
    for j in range(i):
        if board[j]==board[i] or abs(board[i]-board[j])==abs(i-j):
            return False
    return True

def dfs(i):
    if i==n:
        global answer
        answer+=1
        return

    for j in range(n):
        board[i]=j
        if checkBoard(i):
            dfs(i+1)
dfs(0)
print(answer)