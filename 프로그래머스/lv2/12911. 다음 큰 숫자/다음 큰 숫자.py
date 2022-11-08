from collections import Counter
def solution(n):
    temp=n+1
    while Counter((bin(n)[2:]))['1']!=Counter((bin(temp)[2:]))['1']:
        temp+=1
    return temp
