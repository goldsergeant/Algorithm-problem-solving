vowels=['a','e','i','o','u']
while True:
    is_good=True
    s=input()
    if s=='end':
        break

    if all(i not in s for i in vowels):
        is_good=False
    for i in range(2,len(s)):
        if s[i] in vowels and s[i-1] in vowels and s[i-2] in vowels:
            is_good=False
        elif s[i] not in vowels and s[i-1] not in vowels and s[i-2] not in vowels:
            is_good=False
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            if s[i]!='e' and s[i]!='o':
                is_good=False

    print(f'<{s}> is acceptable.' if is_good else f'<{s}> is not acceptable.')