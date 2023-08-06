import itertools

string=input()
answer=[]
for i in range(len(string)-2):
    one=string[:i+1][::-1]
    for j in range(i+1,len(string)-1):
        two=string[i+1:j+1][::-1]
        three=string[j+1:][::-1]
        answer.append(one+two+three)
print(sorted(answer)[0])