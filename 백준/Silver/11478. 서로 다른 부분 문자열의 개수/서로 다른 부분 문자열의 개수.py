import collections
import itertools

s=input()
answer=set()
for i in range(len(s)+1):
    for j in range(len(s)):
        answer.add(s[j:j+i])
print(len(answer)-1)