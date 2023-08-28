s=input()
t=input()
common_mul=len(s)*len(t)
if s*(common_mul//len(s)) == t*(common_mul//len(t)):
    print(1)
else:
    print(0)

