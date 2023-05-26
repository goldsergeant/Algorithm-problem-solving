import collections

n=int(input())
word=None
counter=None
answer=0
for i in range(n):
    if i==0:
        word=list(input())
        word.sort()
    else:
        word2=list(input())
        target=word[:]
        total_diff=0
        for w in word2:
            if w in target:
                target.remove(w)
            else:
                total_diff+=1
        if total_diff<=1 and len(target)<=1:
            answer+=1


print(answer)