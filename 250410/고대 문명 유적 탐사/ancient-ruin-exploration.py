import collections

N=5
ROTATE_N=3
dir=[(-1,0),(1,0),(0,-1),(0,1)]

K,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
item_numbers=list(map(int,input().split()))

def out_check(r,c):
    if r<0 or c<0 or r>=N or c>=N:
        return True
    return False
def rotate_right_90(center_r,center_c):
    tmp_board=[[0 for _ in range(3)] for _ in range(3)]
    tmp_board[1][1]=board[center_r][center_c]

    tmp_r,tmp_c=0,2
    for j in range(center_c-1,center_c+2): # 위 세칸
        tmp_board[tmp_r][tmp_c]=board[center_r-1][j]
        tmp_r+=1

    tmp_r,tmp_c=2,1
    for i in range(center_r,center_r+2): # 오른쪽 두 칸
        tmp_board[tmp_r][tmp_c]=board[i][center_c+1]
        tmp_c-=1

    tmp_r,tmp_c=1,0
    for j in range(center_c,center_c-2,-1): # 밑에 두 칸
        tmp_board[tmp_r][tmp_c]=board[center_r+1][j]
        tmp_r-=1

    tmp_board[0][1]=board[center_r][center_c-1]  # 중간 왼쪽 한 칸

    tmp_r,tmp_c=0,0
    for i in range(center_r-1,center_r+2):
        for j in range(center_c-1,center_c+2):
            board[i][j]=tmp_board[tmp_r][tmp_c]
            tmp_c+=1
        tmp_r+=1
        tmp_c=0

def get_first_items(is_real=False):
    visited=[[False for _ in range(N)] for _ in range(N)]
    cnt=0
    remove_points=[]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                q = collections.deque([(i,j)])
                visited[i][j]=True
                tmp_cnt=0
                tmp_points=[]
                while q:
                    r,c = q.popleft()
                    tmp_cnt+=1
                    tmp_points.append((r,c))
                    for dr,dc in dir:
                        nr,nc=r+dr,c+dc
                        if out_check(nr,nc) or visited[nr][nc] or board[r][c]!=board[nr][nc]:
                            continue
                        visited[nr][nc]=True
                        q.append((nr,nc))



                if tmp_cnt>=3:
                    cnt+=tmp_cnt
                    remove_points.extend(tmp_points)

    if is_real:
        for r,c in remove_points:
            board[r][c]=0
    return cnt

def fill_board():
    global item_fill_idx
    for j in range(N):
        for i in range(N-1,-1,-1):
            if board[i][j]==0:
                board[i][j]=item_numbers[item_fill_idx]
                item_fill_idx+=1


def get_chain_items():
    total_cnt=0
    while True:
        cnt=get_first_items(True)
        if cnt==0:
            break
        total_cnt+=cnt
        fill_board()

    return total_cnt

item_fill_idx=0
for _ in range(K):
    rotate_arr=[]
    for i in range(1,N-1):
        for j in range(1,N-1):
            rotate_cnt=1
            for _ in range(4): #4번을 돌리면 제자리, 단 마지막은 카운트하지 않는다.
                rotate_right_90(i,j)
                if rotate_cnt==4:
                    continue
                first_item_cnt=get_first_items()
                if first_item_cnt>0:
                    rotate_arr.append([first_item_cnt,rotate_cnt,i,j])
                rotate_cnt+=1

    if not rotate_arr:
        break
    rotate_arr.sort(key=lambda x:(-x[0],x[1],-x[3],-x[2]))

    rotate_cnt,rotate_r,rotate_c=rotate_arr[0][1],rotate_arr[0][2],rotate_arr[0][3]
    for _ in range(rotate_cnt):
        rotate_right_90(rotate_r,rotate_c)

    print(get_chain_items(),end=' ')