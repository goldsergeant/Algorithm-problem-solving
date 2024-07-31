import collections

def solution(n, m, x, y, r, c, k):
    visited=[[[False for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    visited[x][y][0]=True
    q=collections.deque([(x,y,'')])
    while q:
        a,b,st=q.popleft()
        if a==r and b==c and len(st)==k:
            return st
        if len(st)==k:
            continue
            
        for da,db,cmd in (1,0,'d'),(0,-1,'l'),(0,1,'r'),(-1,0,'u'):
            na,nb,n_st=a+da,b+db,st+cmd
            if na<1 or nb<1 or na>n or nb>m:
                continue
            distance=abs(na-r)+abs(nb-c)
            if k-len(n_st)<distance or (k-len(n_st)-distance)%2!=0:
                continue
            if not visited[na][nb][len(n_st)]:
                visited[na][nb][len(n_st)]=True
                q.append((na,nb,n_st))
                break
    
    return 'impossible'