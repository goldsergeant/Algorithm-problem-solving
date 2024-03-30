import collections
import sys

while True:
    M = int(sys.stdin.readline())
    if M == 0:
        break
    string = sys.stdin.readline().rstrip()
    char_counter = collections.Counter()
    char_set = set()
    answer = 0
    left=right=-1
    while right<len(string)-1:
        if len(char_set)<M or (len(char_set)==M and char_counter[string[right+1]]>0):
            right+=1
            char_counter[string[right]]+=1
            char_set.add(string[right])
        else:
            left+=1
            char_counter[string[left]]-=1
            if char_counter[string[left]]==0:
                char_set.remove(string[left])
        answer=max(answer,right-left)

    print(answer)
