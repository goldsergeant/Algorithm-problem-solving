import sys

def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    
    answer=sys.maxsize
    words.insert(0,begin)
    visited=[False for _ in range(len(words))]
    target_idx=words.index(target)
    
    def get_diff(a,b):
        diff=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                diff+=1                
        return diff
    
    def dfs(i,depth):
        global answer
        if i==target_idx:
            answer=min(answer,depth)
            return
        
        for j in range(1,len(words)):
            if get_diff(words[i],words[j])==1:
                if not visited[j]:
                    visited[j]=True
                    dfs(j,depth+1)
                    visited[j]=False
 

    visited[0]=True
    dfs(0,0)
    return answer if answer!=sys.maxsize else 0