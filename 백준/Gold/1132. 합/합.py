import collections
import sys

n=int(input())
alphabet_weight=collections.defaultdict(int)
impossible_zero=[]
alphabet_dict=dict()
words=[]

def get_num(word:str):
    mul=1
    return_num=0
    for i in range(len(word)-1,-1,-1):
        return_num+=(alphabet_dict[word[i]]*mul)
        mul*=10

    return return_num

for _ in range(n):
    word=sys.stdin.readline().rstrip()
    impossible_zero.append(word[0])
    words.append(word)
    weight=1
    for i in range(len(word)-1,-1,-1):
        alphabet_weight[word[i]]+=weight
        weight*=10

items=sorted(alphabet_weight.items(),key=lambda x:x[1],reverse=True)
if len(items)==10:
    for i in range(len(items)-1,-1,-1):
        if items[i][0] not in impossible_zero:
            alphabet_weight[items[i][0]]=1
            break


items=sorted(alphabet_weight.items(),key=lambda x:x[1],reverse=True)
num=9
for item in items:
    alphabet_dict[item[0]]=num
    num-=1

answer=0
for i in range(len(words)):
    answer+=get_num(words[i])

print(answer)

