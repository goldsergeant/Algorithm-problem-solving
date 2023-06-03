T=int(input())
for _ in range(T):
    word=list(input())
    target_1, target_2 = -1, 1

    for i in range(len(word)-1,0,-1):
        if word[i]>word[i-1]:
            target_1=i-1
            break

    for i in range(len(word)-1,0,-1):
        if word[i]>word[target_1]:
            target_2=i
            break
    if target_1!=-1:
        word[target_1],word[target_2]=word[target_2],word[target_1]
        word[target_1+1:]=sorted(word[target_1+1:])
    print(''.join(word))