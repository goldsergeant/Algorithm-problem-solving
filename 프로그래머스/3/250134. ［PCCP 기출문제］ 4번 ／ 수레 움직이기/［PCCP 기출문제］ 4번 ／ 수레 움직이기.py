import sys

def solution(maze):
    global answer
    
    def dfs(red_r,red_c,blue_r,blue_c,depth):
        global answer
        if red_visited[red_end_r][red_end_c] and blue_visited[blue_end_r][blue_end_c]:
            answer=min(answer,depth)
            return
        
        n_red_arr=[]
        n_blue_arr=[]
        if (red_r,red_c)!=(red_end_r,red_end_c):
            for dr,dc in (0,-1),(0,1),(-1,0),(1,0):
                n_red_r,n_red_c = red_r+dr,red_c+dc
                if n_red_r<0 or n_red_c<0 or n_red_r>=len(maze) or n_red_c>=len(maze[0]):
                    continue
                if red_visited[n_red_r][n_red_c] or maze[n_red_r][n_red_c]==5:
                    continue
                n_red_arr.append((n_red_r,n_red_c))
                
        if (blue_r,blue_c)!=(blue_end_r,blue_end_c):
            for dr,dc in (0,-1),(0,1),(-1,0),(1,0):
                n_blue_r,n_blue_c = blue_r+dr,blue_c+dc
                if n_blue_r<0 or n_blue_c<0 or n_blue_r>=len(maze) or n_blue_c>=len(maze[0]):
                    continue
                if blue_visited[n_blue_r][n_blue_c] or maze[n_blue_r][n_blue_c]==5:
                    continue
                n_blue_arr.append((n_blue_r,n_blue_c))
        
        if n_red_arr and n_blue_arr:
            for r_r,r_c in n_red_arr:
                red_visited[r_r][r_c]=True
                for b_r,b_c in n_blue_arr:
                    if (r_r,r_c)==(blue_r,blue_c) and (b_r,b_c)==(red_r,red_c):
                        continue
                    if (r_r,r_c)==(b_r,b_c):
                        continue
                        
                    blue_visited[b_r][b_c]=True
                    dfs(r_r,r_c,b_r,b_c,depth+1)
                    blue_visited[b_r][b_c]=False
                red_visited[r_r][r_c]=False
                
        elif n_red_arr:
            for r_r,r_c in n_red_arr:
                if (r_r,r_c)!=(blue_r,blue_c):
                    red_visited[r_r][r_c]=True
                    dfs(r_r,r_c,blue_r,blue_c,depth+1)
                    red_visited[r_r][r_c]=False
        
        elif n_blue_arr:
            for b_r,b_c in n_blue_arr:
                if (b_r,b_c)!=(red_r,red_c):
                    blue_visited[b_r][b_c]=True
                    dfs(red_r,red_c,b_r,b_c,depth+1)
                    blue_visited[b_r][b_c]=False
        
    answer = sys.maxsize
    red_visited=[[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    blue_visited=[[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    red_start_r,red_start_c=0,0
    blue_start_r,blue_start_c=0,0
    red_end_r,red_end_c=0,0
    blue_end_r,blue_end_c=0,0
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j]==1:
                red_start_r,red_start_c=i,j
            elif maze[i][j]==2:
                blue_start_r,blue_start_c=i,j
            elif maze[i][j]==3:
                red_end_r,red_end_c=i,j
            elif maze[i][j]==4:
                blue_end_r,blue_end_c=i,j
                
    red_visited[red_start_r][red_start_c]=True
    blue_visited[blue_start_r][blue_start_c]=True
    dfs(red_start_r,red_start_c,blue_start_r,blue_start_c,0)
        
    return answer if answer!=sys.maxsize else 0