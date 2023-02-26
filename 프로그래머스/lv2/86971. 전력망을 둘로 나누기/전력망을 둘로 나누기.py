import sys
import collections
def solution(n, wires):
    answer=[]
    for remove_index in range(len(wires)):
        visited=[False for i in range(n+1)]
        return_cnt=[]
        def bfs(start:int)->int:
            count=1
            queue=collections.deque()
            queue.appendleft(start)
            while queue:
                next=queue.pop()
                visited[next]=True
                count+=1
                for node in graph[next]:
                    if not visited[node]:
                        visited[node]=True
                        queue.appendleft(node)
            return count
            
        graph=collections.defaultdict(list)
        for i in range(len(wires)):
            if i!=remove_index:
                a,b=wires[i][0],wires[i][1]
                graph[a].append(b)
                graph[b].append(a)
        
        for i in range(1,n+1):
            if not visited[i]:
                return_cnt.append(bfs(i))
        answer.append(abs(return_cnt[0]-return_cnt[1]))
        
    return min(answer)
    