import collections
import sys

n=int(input())
dic=collections.defaultdict(int)
for _ in range(n):
    file=sys.stdin.readline().rstrip()
    name,extension=file.split('.')
    dic[extension]+=1


for key in sorted(dic.keys()):
    print(f'{key} {dic[key]}')