import collections

def solution(survey, choices):
    answer = ''
    mbti_score=collections.defaultdict(int)
    for i in range(len(survey)):
        negative,positive=survey[i][0],survey[i][1]
        if choices[i]==1:
            mbti_score[negative]+=3
        elif choices[i]==2:
            mbti_score[negative]+=2
        elif choices[i]==3:
            mbti_score[negative]+=1
        elif choices[i]==5:
            mbti_score[positive]+=1
        elif choices[i]==6:
            mbti_score[positive]+=2
        elif choices[i]==7:
            mbti_score[positive]+=3
            
    finally_mbti=[]
    finally_mbti.append('R' if mbti_score['R']>=mbti_score['T'] else 'T')
    finally_mbti.append('C' if mbti_score['C']>=mbti_score['F'] else 'F')
    finally_mbti.append('J' if mbti_score['J']>=mbti_score['M'] else 'M')
    finally_mbti.append('A' if mbti_score['A']>=mbti_score['N'] else 'N')
    print(mbti_score)
    return ''.join(finally_mbti)