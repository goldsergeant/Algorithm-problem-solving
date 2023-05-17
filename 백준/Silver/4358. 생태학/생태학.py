import collections
import sys

total=0
trees=collections.defaultdict(int)
while True:
    word=sys.stdin.readline().strip()
    if word=='':
        break
    total+=1
    trees[word]+=1

for tree in sorted(trees.keys()):
    print('%s %.4f' %(tree,trees[tree]/total*100))