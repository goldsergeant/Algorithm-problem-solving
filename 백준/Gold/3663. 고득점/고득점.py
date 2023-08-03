import collections
import string
import sys
from copy import deepcopy


t=int(input())
for _ in range(t):
    target=list(sys.stdin.readline().rstrip())
    answer=0
    min_move=len(target)-1

    for char in target:
        answer+=min(ord(char)-ord('A'),ord('Z')-ord(char)+1)


    for i in range(len(target)):
        j=i+1
        while j<len(target) and target[j]=='A': # 바로 다음 'A'가 아닌 자리 찾기
            j+=1

        min_move=min(min_move,2*i+len(target)-j,2*(len(target)-j)+i)

    answer+=min_move
    print(answer)