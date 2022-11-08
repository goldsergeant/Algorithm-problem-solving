class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=collections.defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        traced=set()
        visited=set()
        def dfs(a):
            if a in traced:
                return False
            if a in visited:
                return True
            traced.add(a)
            for y in graph[a]:
                if not dfs(y):
                    return False
            traced.remove(a)
            visited.add(a)
            
            return True
            
        for x in list(graph):
            if not dfs(x):
                return False
        return True
            