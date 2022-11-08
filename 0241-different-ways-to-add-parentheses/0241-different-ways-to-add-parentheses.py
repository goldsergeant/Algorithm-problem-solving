class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results=[]
        if expression.isdigit():
            return [int(expression)]
        for index,value in enumerate(expression):
            if value in '-*+':
                left=self.diffWaysToCompute(expression[:index])
                right=self.diffWaysToCompute(expression[index+1:])
                
                for l in left:
                    for r in right:
                        results.append(eval(str(l)+value+str(r)))
        return results