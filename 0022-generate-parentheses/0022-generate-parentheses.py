class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer=[]
        def generate(st:str,left:int,right:int):
            if left==0 and right==0:
                answer.append(st)
            if left>0:
                generate(st+'(',left-1,right)
            if right>0 and left<right:
                generate(st+')',left,right-1)
        generate('',n,n)
        return answer