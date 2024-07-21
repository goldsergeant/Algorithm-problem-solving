def check(user,banned):
    if len(user)!=len(banned):
        return False
    
    for i in range(len(user)):
        if banned[i]=='*':
            continue
        if user[i]!=banned[i]:
            return False
    
    return True


def solution(user_id, banned_id):
    visited=[False for _ in range(len(user_id))]
    global answer
    answer=set()
    def dfs(idx,ids):
        global answer
        if idx==len(banned_id):
            answer.add(tuple(sorted(ids)))
            return
        
        for i in range(len(user_id)):
            if check(user_id[i],banned_id[idx]) and not visited[i]:
                visited[i]=True
                dfs(idx+1, ids+[user_id[i]])
                visited[i]=False
                
    
    dfs(0,[])
    print(answer)
    return len(answer)