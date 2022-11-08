class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        pos=0
        for char in reversed(columnTitle):
            digit=ord(char)-64
            result+=digit*26**pos
            pos+=1
        return result
            