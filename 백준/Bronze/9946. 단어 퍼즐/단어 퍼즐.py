import collections
import sys

idx=1
while True:
    a=sys.stdin.readline().rstrip()
    b=sys.stdin.readline().rstrip()

    if a=='END' and b=='END':
        break

    if collections.Counter(a)==collections.Counter(b):
        print(f'Case {idx}: same')
    else:
        print(f'Case {idx}: different')

    idx+=1