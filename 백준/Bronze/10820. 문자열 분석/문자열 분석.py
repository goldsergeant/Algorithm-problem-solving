import sys

while True:
    s=sys.stdin.readline().rstrip('\n')
    if not s:
        break

    lower=upper=number=space=0
    for char in s:
        if char.islower():
            lower+=1
        elif char.isupper():
            upper+=1
        elif char.isnumeric():
            number+=1
        elif char.isspace():
            space+=1
    print('%d %d %d %d' %(lower,upper,number,space))