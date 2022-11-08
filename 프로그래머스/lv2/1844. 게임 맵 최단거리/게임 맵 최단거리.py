import collections
def solution(maps):
    queue=collections.deque()
    queue.append((0,0,1))
    
    while queue:
        temp=queue.popleft()
        
        if temp[0]==len(maps)-1 and temp[1]==len(maps[0])-1:
            return temp[2]
        
        if temp[0]<len(maps)-1 and maps[temp[0]+1][temp[1]]!=0:
            queue.append((temp[0]+1,temp[1],temp[2]+1))
            maps[temp[0]+1][temp[1]]=0
        if temp[1]<len(maps[0])-1 and maps[temp[0]][temp[1]+1]!=0:
            queue.append((temp[0],temp[1]+1,temp[2]+1))
            maps[temp[0]][temp[1]+1]=0
        if temp[0]>0 and maps[temp[0]-1][temp[1]]!=0:
            queue.append((temp[0]-1,temp[1],temp[2]+1))
            maps[temp[0]-1][temp[1]]=0
        if temp[1]>0 and maps[temp[0]][temp[1]-1]!=0:
            queue.append((temp[0],temp[1]-1,temp[2]+1))
            maps[temp[0]][temp[1]-1]=0
    
    return -1
        