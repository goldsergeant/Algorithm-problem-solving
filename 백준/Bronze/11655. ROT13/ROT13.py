import collections
import string

lower_case=list(string.ascii_lowercase)
upper_case=list(string.ascii_uppercase)

s=list(input())
for i in range(len(s)):
    if s[i].isalpha():
        if s[i].isupper():
            s[i]=upper_case[(upper_case.index(s[i])+13)%len(upper_case)]

        elif s[i].islower():
            s[i] = lower_case[(lower_case.index(s[i]) + 13) % len(lower_case)]
print(''.join(s))

