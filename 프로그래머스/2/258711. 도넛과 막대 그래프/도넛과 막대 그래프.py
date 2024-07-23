import collections

def solution(edges):
    indegree=collections.defaultdict(int)
    outdegree=collections.defaultdict(int)
    nodes=set()
    tmp_node=0
    graph=collections.defaultdict(list)
    visited=collections.defaultdict(bool)
    answer=[0,0,0,0]
    
    for u,v in edges:
        indegree[v]+=1
        outdegree[u]+=1
        nodes.update([u,v])
        if u==v:
            visited[u]=True
            answer[1]+=1
        graph[u].append(v)
        if indegree[u]==0 and outdegree[u]>=2:
            tmp_node=u
            answer[0]=tmp_node
            nodes.remove(tmp_node)
        
    for u,v in edges:
        if u==tmp_node:
            indegree[v]-=1
            outdegree[u]-=1
            

    for node in nodes:
        answer_idx=0
        if visited[node]: 
            continue
            
        if outdegree[node]==2:
            answer_idx=3
        elif indegree[node]==0:
            answer_idx=2
        else:
            continue
        
        q=collections.deque([node])
        visited[node]=True
        
        while q:
            i=q.popleft()
            for j in graph[i]:
                if not visited[j]:
                    visited[j]=True
                    q.append(j)
        answer[answer_idx]+=1
        
    for node in nodes:
        if not visited[node]:
            visited[node]=True
            q=collections.deque([node])
            
            while q:
                i=q.popleft()
                for j in graph[i]:
                    if not visited[j]:
                        visited[j]=True
                        q.append(j)
            answer[1]+=1
    return answer