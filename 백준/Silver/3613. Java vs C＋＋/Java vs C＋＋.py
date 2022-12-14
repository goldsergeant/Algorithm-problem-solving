import string

st = input()
answer = []
i = 0

def isInUp(str: string) -> bool:
    for char in str:
        if char.isupper():
            return True
    return False

if st[-1] == '_':
    print("Error!")
    exit()
elif st[0] == "_":
    print("Error!")
    exit()
elif '__' in st:
    print("Error!")
    exit()
elif '_' in st and isInUp(st):
    print("Error!")
    exit()
elif st[0].isupper():
    print("Error!")
    exit()
if '_' in st:
    while i < len(st):
        if i == 0 and st[i].islower():
            answer.append(st[i])
        elif st[i] == "_":
            i += 1
            continue
        elif st[i - 1] == "_":
            answer.append(st[i].upper())
        else:
            answer.append(st[i])
        i += 1
elif '_' not in st:
    while i < len(st):
        if i == 0 and st[i].islower():
            answer.append(st[i])
        elif st[i].isupper():
            answer.append('_' + st[i].lower())
        else:
            answer.append(st[i])
        i += 1
print(''.join(answer))

