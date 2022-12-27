n = int(input())
s = int(input())
m = input()
answer = 0
point = 0
count = 0
while point < s:
    if m[point:point + 3] == 'IOI':
        point += 2
        count += 1
        if count == n:
            answer+=1
            count-=1
    else:
        point+=1
        count=0
print(answer)
