from itertools import combinations as comby
def solution(nums):
    def primeNumber(n:int):
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    answer=0
    cb=comby(nums,3)
    for c in cb:
        if primeNumber(sum(c)):
            answer+=1
    return answer
    