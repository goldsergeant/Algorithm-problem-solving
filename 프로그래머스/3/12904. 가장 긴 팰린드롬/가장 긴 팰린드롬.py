def solution(s):
    cache=[[-1 for _ in range(len(s))] for _ in range(len(s))]

    def dfs(left, right):
        if left == right:
            return 1
        if left+1 == right:
            return 0 if s[left]!=s[right] else 2
        if cache[left][right]!=-1:
            return cache[left][right]

        cache[left][right]= dfs(left+1, right-1) if s[left]==s[right] else 0
        return cache[left][right]

    answer=0
    for l in range(1,len(s)+1):
        for i in range(len(s)-l+1):
            if dfs(i,i+l-1):
                answer=max(answer,l)

    return answer