class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[]
        for i in range(rowIndex+1):
            result.append([])
            result[i].append(1)
            for j in range(1,i):
                result[i].append(result[i-1][j-1]+result[i-1][j])
            if i!=0:
                result[i].append(1)
        return result[rowIndex]