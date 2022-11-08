class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=collections.Counter(s1)
        missing=len(s1)
        
        for i in range(len(s2)):
            if s2[i] in need:
                need[s2[i]]-=1
            if i>=missing and s2[i-missing] in need:
                need[s2[i-missing]]+=1
            if all([need[char]==0 for char in need]):
                return True
        return False