import sys
import collections
dir=[(0,-1),(0,1),(1,0),(-1,0)]

def in_check(n,m,r,c):
    if r<0 or c<0 or r>=n or c>=m:
        return False
    return True

def solution(maze):
    answer=0
    n,m=len(maze),len(maze[0])
    
    q=collections.deque()
    s_red_r,s_red_c,s_blue_r,s_blue_c=0,0,0,0
    end_red_r,end_red_c,end_blue_r,end_blue_c=0,0,0,0
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j]==1:
                s_red_r,s_red_c=i,j
            elif maze[i][j]==2:
                s_blue_r,s_blue_c=i,j
            elif maze[i][j]==3:
                end_red_r,end_red_c=i,j
            elif maze[i][j]==4:
                end_blue_r,end_blue_c=i,j
                
    q.append((s_red_r,s_red_c,s_blue_r,s_blue_c,set([(s_red_r,s_red_c)]),set([(s_blue_r,s_blue_c)])))
    while q:
        for _ in range(len(q)):
            red_r,red_c,blue_r,blue_c,red_visited,blue_visited=q.popleft()
            print(red_r,red_c,blue_r,blue_c)
            if (red_r,red_c,blue_r,blue_c)==(end_red_r,end_red_c,end_blue_r,end_blue_c):
                return answer
            
            if (red_r,red_c)==(end_red_r,end_red_c):
                for dr,dc in dir:
                    n_blue_r,n_blue_c=blue_r+dr,blue_c+dc
                    if not in_check(n,m,n_blue_r,n_blue_c):
                        continue
                    if (n_blue_r,n_blue_c) in blue_visited:
                        continue
                    if maze[n_blue_r][n_blue_c]==5:
                        continue
                    if (n_blue_r,n_blue_c)==(red_r,red_c):
                        continue
                    n_blue_visited=blue_visited|set([(n_blue_r,n_blue_c)])
                    q.append((red_r,red_c,n_blue_r,n_blue_c,red_visited,n_blue_visited))
                    
            elif (blue_r,blue_c)==(end_blue_r,end_blue_c):
                for dr,dc in dir:
                    n_red_r,n_red_c=red_r+dr,red_c+dc
                    if not in_check(n,m,n_red_r,n_red_c):
                        continue
                    if (n_red_r,n_red_c) in red_visited:
                        continue
                    if maze[n_red_r][n_red_c]==5:
                        continue
                    if (n_red_r,n_red_c)==(blue_r,blue_c):
                        continue
                        
                    n_red_visited=red_visited|set([(n_red_r,n_red_c)])
                    q.append((n_red_r,n_red_c,blue_r,blue_c,n_red_visited,blue_visited))
            else:
                for dr1,dc1 in dir:
                    n_red_r,n_red_c=red_r+dr1,red_c+dc1
                    if not in_check(n,m,n_red_r,n_red_c):
                        continue
                    for dr2,dc2 in dir:
                        n_blue_r,n_blue_c=blue_r+dr2,blue_c+dc2
                        if not in_check(n,m,n_blue_r,n_blue_c):
                            continue
                        if (n_red_r,n_red_c)==(n_blue_r,n_blue_c):
                            continue
                        if (n_red_r,n_red_c) in red_visited or (n_blue_r,n_blue_c) in blue_visited:
                            continue
                        if maze[n_red_r][n_red_c]==5 or maze[n_blue_r][n_blue_c]==5:
                            continue
                        if (n_blue_r,n_blue_c,n_red_r,n_red_c)==(red_r,red_c,blue_r,blue_c):
                            continue

                        n_red_visited=red_visited|set([(n_red_r,n_red_c)])
                        n_blue_visited=blue_visited|set([(n_blue_r,n_blue_c)])
                        q.append((n_red_r,n_red_c,n_blue_r,n_blue_c,n_red_visited,n_blue_visited))
        
        answer+=1
        
        
    return 0