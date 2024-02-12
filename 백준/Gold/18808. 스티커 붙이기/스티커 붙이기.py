import sys

N, M, K = map(int, sys.stdin.readline().split())
notebook=[[0 for _ in range(M)] for _ in range(N)]
answer=0

def rotate_right(sticker):
    new_sticker=[]

    for j in range(len(sticker[0])):
        temp=[]
        for i in range(len(sticker)-1,-1,-1):
            temp.append(sticker[i][j])
        new_sticker.append(temp)

    return new_sticker

def can_attach_sticker(sticker,r,c):
    for i in range(r,r+len(sticker)):
        for j in range(c,c+len(sticker[0])):
            if i>=N or i<0 or j>=M or j<0 or (notebook[i][j]==1 and sticker[i-r][j-c]==1):
                return False

    return True

def attach_sticker(sticker,r,c):
    for i in range(r,r+len(sticker)):
        for j in range(c,c+len(sticker[0])):
            if sticker[i-r][j-c]==1:
                notebook[i][j]=sticker[i-r][j-c]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    sticker=[list(map(int, sys.stdin.readline().split())) for _ in range(r)]
    is_executed=False
    for _ in range(4):
        for i in range(N):
            for j in range(M):
                if can_attach_sticker(sticker,i,j):
                    attach_sticker(sticker,i,j)
                    is_executed=True
                    break
            if is_executed:
                break
        if is_executed:
            break
        sticker=rotate_right(sticker)


for i in range(N):
    for j in range(M):
        if notebook[i][j]==1:
            answer+=1
print(answer)
