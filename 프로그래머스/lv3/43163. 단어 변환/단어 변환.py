def solution(begin, target, words):
    def getDiff(word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        return count
    answer=[]
    visited=[]
    def dfs(word, reps,visited):
        if word in visited:
            return
        visited.append(word)
        if target not in words:
            answer.append(0)
            return
        if word == target:
            answer.append(reps)
            return
        for i in range(len(words)):
            if getDiff(word, words[i]) == 1:
                dfs(words[i], reps + 1,visited)
    dfs(begin, 0,visited)
    return min(answer) if answer else 0