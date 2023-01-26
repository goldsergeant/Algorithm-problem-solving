class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        output=0
        g.sort()
        s.sort()
        
        ch=0
        cookie=0
        while ch<len(g) and cookie<len(s):
            if g[ch]<=s[cookie]:
                output+=1
                ch+=1
            cookie+=1
        return output