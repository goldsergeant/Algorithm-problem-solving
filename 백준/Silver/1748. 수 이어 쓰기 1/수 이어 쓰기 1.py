n=int(input())
answer=0
while n>0:
    l=len(str(n))
    diff_num=n-int('9'*(l-1) if l>1 else '0')
    answer+=diff_num*l
    n-=diff_num
print(answer)