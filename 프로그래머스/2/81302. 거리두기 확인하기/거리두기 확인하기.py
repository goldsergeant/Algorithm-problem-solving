import collections

def solution(places):
    answer = []
    def bfs(s_r,s_c,place):
        q=collections.deque([(s_r,s_c)])
        visited=[[False for _ in range(5)] for _ in range(5)]
        visited[s_r][s_c]=True
        
        for _ in range(3):
            for _ in range(len(q)):
                r,c=q.popleft()
                if (r,c)!=(s_r,s_c) and place[r][c]=='P':
                    return False
                
                for dr,dc in (0,-1),(0,1),(1,0),(-1,0):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc] and place[nr][nc]!='X':
                        visited[nr][nc]=True
                        q.append((nr,nc))
        
        return True
    
    def check_place(place):
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j]=='P':
                    if not bfs(i,j,place):
                        return 0
        return 1
    
    for place in places:
        answer.append(check_place(place))
                                 
    return answer