import sys

A,B=input().split()

answer=sys.maxsize
for i in range(len(B)-len(A)+1):
    diff=0
    temp=B[i:]
    for j in range(len(A)):
        if A[j]!=temp[j]:
            diff+=1

    answer=min(answer,diff)

print(answer)

