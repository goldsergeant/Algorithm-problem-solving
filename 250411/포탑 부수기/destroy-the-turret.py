import collections

lazer_dir=[(0,1),(1,0),(0,-1),(-1,0)] #우하좌상
bomb_dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
def get_weakest_canon():
    tmp_arr=[]

    for i in range(N):
        for j in range(M):
            if canons[i][j]>0:
                tmp_arr.append((canons[i][j],recent_attacks[i][j],i,j))

    tmp_arr.sort(key=lambda x:(x[0],-x[1],-(x[2]+x[3]),-x[3]))

    return tmp_arr[0][2],tmp_arr[0][3]

def get_strongest_canon():
    tmp_arr = []

    for i in range(N):
        for j in range(M):
            if canons[i][j] > 0:
                tmp_arr.append((canons[i][j], recent_attacks[i][j], i, j))

    tmp_arr.sort(key=lambda x: (-x[0], x[1], (x[2] + x[3]), x[3]))

    return tmp_arr[0][2], tmp_arr[0][3]
def get_attackable_canon():
    attacakable_canon_cnt=0
    for i in range(N):
        for j in range(M):
            if canons[i][j]>0:
                attacakable_canon_cnt+=1

    return attacakable_canon_cnt

def convert_points(r,c): # 좌표가 가장자리밖으로 넘어가면 변환해주는 함수
    if r==-1:
        r=N-1
    elif r==N:
        r=0

    if c==-1:
        c=M-1
    elif c==M:
        c=0

    return r,c

def get_path_by_lazer(w_r, w_c, s_r, s_c):
    q=collections.deque([(w_r,w_c,[])])
    visited=[[False for _ in range(M)] for _ in range(N)]
    visited[w_r][w_c]=True

    while q:
        r,c,path=q.popleft()
        if (r,c)==(s_r,s_c):
            return path

        for dr,dc in lazer_dir:
            nr,nc=convert_points(r+dr,c+dc)
            if visited[nr][nc] or canons[nr][nc]==0:
                continue
            visited[nr][nc]=True
            q.append((nr,nc,path+[(nr,nc)]))

    return None

def attack_by_lazer(w_r,w_c,attack,path,turn):
    recent_attacks[w_r][w_c]=turn
    for i in range(len(path)):
        r,c=path[i]
        if i==len(path)-1:
            canons[r][c]-=attack
        else:
            canons[r][c]-=(attack//2)

def attack_by_bomb(w_r,w_c,s_r,s_c,attack,turn):
    recent_attacks[w_r][w_c]=turn
    canons[s_r][s_c]-=attack
    for dr,dc in bomb_dir:
        nr,nc=s_r+dr,s_c+dc
        if (nr<0 or nr>=N) and (nc<0 or nc>=M):
            continue
        nr,nc=convert_points(s_r+dr,s_c+dc)
        if (nr,nc)!=(s_r,s_c):
            canons[nr][nc]-=(attack//2)

def fix_unrelated_canons():
    for i in range(N):
        for j in range(M):
            if is_unrelated_canons[i][j] and canons[i][j]>0:
                canons[i][j]+=1

def clear_breaked_canons(): # 부서진포탑들은 0으로 정리
    for i in range(N):
        for j in range(M):
            if canons[i][j]<0:
                canons[i][j]=0

N,M,K=map(int,input().split())
canons=[list(map(int,input().split())) for _ in range(N)]
recent_attacks=[[0 for _ in range(M)] for _ in range(N)]
for cur_turn in range(1,K+1):
    if get_attackable_canon()==1:
        break
    is_unrelated_canons=[[True for _ in range(M)] for _ in range(N)]
    w_r,w_c=get_weakest_canon()
    s_r,s_c=get_strongest_canon()
    lazer_path=get_path_by_lazer(w_r,w_c,s_r,s_c)
    canons[w_r][w_c]+=(N+M)

    is_unrelated_canons[w_r][w_c]=False
    is_unrelated_canons[s_r][s_c]=False
    if not lazer_path: # 포탑 공격
        for dr,dc in bomb_dir:
            r,c=convert_points(s_r+dr,s_c+dc)
            if (r<0 or r>=N) and (c<0 or c>=M): # 둘다 범위를 벗어날 경우 가장자리가 아닌 모서리
                continue

            if canons[r][c]>0:
                is_unrelated_canons[r][c]=False

        attack_by_bomb(w_r,w_c,s_r,s_c,canons[w_r][w_c],cur_turn)
    else:
        attack_by_lazer(w_r,w_c,canons[w_r][w_c],lazer_path,cur_turn)
        for r,c in lazer_path:
            is_unrelated_canons[r][c]=False

    clear_breaked_canons()
    fix_unrelated_canons()

last_s_r,last_s_c=get_strongest_canon()
print(canons[last_s_r][last_s_c])