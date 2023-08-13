import sys

n,r,c=map(int,sys.stdin.readline().split())
answer=0
def divide(row,col,size):
    global answer
    if row==r and col==c:
        print(answer)
        exit()

    if r<row+size and r>=row and c<col+size and c>=col:
        divide(row,col,size//2)
        divide(row,col+size//2,size//2)
        divide(row+size//2,col,size//2)
        divide(row+size//2,col+size//2,size//2)
    else:
        answer+=size**2

divide(0,0,2**n)