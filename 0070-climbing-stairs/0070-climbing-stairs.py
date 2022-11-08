class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        one,two=1,1
        for _ in range(n):
            one,two=two,one+two
        return one
            