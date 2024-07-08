import collections
import sys

N=int(sys.stdin.readline())
word_cnt_dict=collections.defaultdict(int)
for _ in range(N):
    word=sys.stdin.readline().rstrip()
    if len(word)==1:
        word_cnt_dict[word]+=1
    else:
        middle=''.join(sorted(word[1:-1]))
        word=word[0]+middle+word[-1]
        word_cnt_dict[word]+=1

M=int(sys.stdin.readline())
for _ in range(M):
    words=sys.stdin.readline().rstrip().split()
    answer=1
    for word in words:
        if len(word)==1:
            answer*=word_cnt_dict[word]
        else:
            middle = ''.join(sorted(word[1:-1]))
            word = word[0] + middle + word[-1]
            answer*=word_cnt_dict[word]

    print(answer)