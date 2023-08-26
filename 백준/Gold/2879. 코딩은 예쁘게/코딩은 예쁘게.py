import sys

n=int(input())
cur_tab=list(map(int,input().split()))
correct_tab=list(map(int,input().split()))
answer=0

i=0
while i<n:
    if cur_tab[i]<correct_tab[i]:
        j=i
        while j<n and cur_tab[j]<correct_tab[j]:
            j+=1
        plus_num=min(abs(correct_tab[k]-cur_tab[k]) for k in range(i,j))
        answer+=plus_num
        for k in range(i,j):
            cur_tab[k]+=plus_num

    elif cur_tab[i]>correct_tab[i]:
        j=i
        while j<n and cur_tab[j]>correct_tab[j]:
            j+=1
        minus_num=min(abs(correct_tab[k]-cur_tab[k]) for k in range(i,j))
        answer+=minus_num
        for k in range(i,j):
            cur_tab[k]-=minus_num

    else:
        i+=1


print(answer)
