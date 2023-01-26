class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            answer=int(str(x)[::-1])
            if answer>2**31:
                return 0
            else:
                return answer
        else:
            answer=-int(str(x)[-1:0:-1])
            if answer<-2**31:
                return 0
            else:
                return answer