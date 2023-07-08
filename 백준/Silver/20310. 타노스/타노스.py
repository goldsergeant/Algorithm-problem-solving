import collections

s=list(input())
remove_zero_count=s.count('0')//2
remove_one_count=s.count('1')//2

for i in range(len(s)-1,-1,-1):
    if remove_zero_count==0:
        break
    if s[i]=='0':
        s[i]='#'
        remove_zero_count-=1

for i in range(len(s)):
    if remove_one_count==0:
        break
    if s[i]=='1':
        s[i]='#'
        remove_one_count-=1

print(''.join(filter(lambda c:c!='#',s)))





