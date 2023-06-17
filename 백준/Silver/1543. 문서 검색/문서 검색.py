s1=input()
s2=input()

answer=0
while s2 in s1:
    s1=s1.replace(s2,'#',1)
    answer+=1
print(answer)