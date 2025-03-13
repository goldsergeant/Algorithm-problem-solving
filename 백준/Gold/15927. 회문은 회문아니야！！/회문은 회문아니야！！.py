import sys

string=sys.stdin.readline().strip()

answer=0
if len(set(string))==1:
    answer=-1
elif string==string[::-1]:
    answer=len(string)-1
else:
    answer=len(string)

print(answer)