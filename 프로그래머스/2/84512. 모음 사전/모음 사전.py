def solution(word):
    total_words=[]
    def dfs(text):
        if len(text)>0:
            total_words.append(text)

        if len(text)<5:
            for ch in ['A','E','I','O','U']:
                dfs(text+ch)

    dfs('')
    return total_words.index(word)+1

