class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        output=[]
        for char in digits:
            s+=str(char)
        s=int(s)+1
        for char in str(s):
            output.append(int(char))
        return output