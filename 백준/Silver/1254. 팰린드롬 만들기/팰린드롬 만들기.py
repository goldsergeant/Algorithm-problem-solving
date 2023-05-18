S=input()
idx=0
while S[idx:]!=''.join(reversed(S[idx:])):
    idx+=1

print(len(S)+idx)







