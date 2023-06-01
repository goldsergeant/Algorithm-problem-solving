s = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer=0
for word in croatia:
    if word in s:
        answer+=s.count(word)
        s=s.replace(word,'*')

for char in s:
    if char!='*':
        answer+=1
print(answer)
