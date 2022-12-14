class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size):
            for i in range(start+1,start+size+1):
                if i>=len(data) or (data[i]>>6)!=0b10:
                    return False
            return True
        
        start=0
        while start<len(data):
            if data[start]>>3==0b11110 and check(3):
                start+=4
            elif data[start]>>4==0b1110 and check(2):
                start+=3
            elif data[start]>>5==0b110 and check(1):
                start+=2
            elif data[start]>>7==0:
                start+=1
            else:
                return False
        return True