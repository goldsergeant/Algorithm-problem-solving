import collections


def solution(cacheSize, cities):
    answer = 0
    cache=collections.deque(maxlen=cacheSize)
    cities=list(map(lambda x:x.lower(),cities))

    for idx,city in enumerate(cities):
        if city in cache:
            answer+=1
            cache.remove(city)
            cache.append(city)
        else:
            answer+=5
            cache.append(city)

    return answer