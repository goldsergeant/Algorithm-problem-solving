class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_count=collections.Counter(s)
        second_count=collections.Counter(t)
        if first_count==second_count:
            return True
        return False