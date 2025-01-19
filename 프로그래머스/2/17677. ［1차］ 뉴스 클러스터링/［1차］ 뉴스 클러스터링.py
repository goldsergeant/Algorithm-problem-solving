import collections


def solution(str1, str2):
    answer = 0
    str1_set = []
    str2_set = []

    for i in range(1, len(str1)):
        if str1[i - 1].isalpha() and str1[i].isalpha():
            str1_set.append((str1[i - 1] + str1[i]).lower())

    for i in range(1, len(str2)):
        if str2[i - 1].isalpha() and str2[i].isalpha():
            str2_set.append((str2[i - 1] + str2[i]).lower())

    try:
        counter1=collections.Counter(str1_set)
        counter2=collections.Counter(str2_set)
        union_counter=collections.Counter()
        intersection_counter=collections.Counter()
        union=[]
        intersection=[]
        for string in str1_set+str2_set:
            if union_counter[string]<max(counter1[string],counter2[string]):
                union_counter[string]+=1
                union.append(string)

            if intersection_counter[string]<min(counter1[string],counter2[string]):
                intersection_counter[string]+=1
                intersection.append(string)

        answer=int(len(intersection)/len(union)*65536)
    except ZeroDivisionError:
        return 65536
    return answer