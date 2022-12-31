import collections

st=input()
counter=collections.Counter(st)

odd_char=""
for key in sorted(counter.keys()):
    if counter[key]%2==1:
        if odd_char=="":
            odd_char=key
        else:
            print("I'm Sorry Hansoo")
            exit()

answer=""

for key in sorted(counter.keys()):
    count=counter[key]//2
    answer+=key*count

temp=answer
answer+=odd_char
answer+=temp[::-1]
print(answer)
