T=int(input())

def is_palindrome(word,left,right):
    while left<right:
        if word[left]==word[right]:
            left+=1
            right-=1
        else:
            return False
    return True

def check_st(s:str):
    if is_palindrome(s,0,len(s)-1):
        return 0

    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            if is_palindrome(s,left+1,right) or  is_palindrome(s,left,right-1):
                return 1
            else:
                return 2
        left+=1
        right-=1


for _ in range(T):
    s=input()
    print(check_st(s))