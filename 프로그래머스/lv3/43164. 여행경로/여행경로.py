def solution(tickets):
    tickets.sort(key=lambda x:(x[0],x[1]))
    global check
    check=False
    answer=[]
    visited=[False for i in range(len(tickets))]
    def dfs(node,depth):
        global check
        if depth==len(tickets):
            check=True
        answer.append(node)

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0]==node:
                visited[i]=True
                dfs(tickets[i][1],depth+1)
                if not check:
                    answer.pop()
                    visited[i]=False
    dfs("ICN",0)
    return answer