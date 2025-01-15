from heapq import heappush, heappop

def solution(cacheSize, cities):
    answer = 0
    cache=dict()
    cities=list(map(lambda x:x.lower(),cities))

    for idx,city in enumerate(cities):
        if city in cache:
            answer += 1
            cache[city]=len(cities)-idx
        else:
            answer+=5
            if len(cache)<cacheSize:
                cache[city]=len(cities)-idx
            else:
                remove_cache_city=''
                recent_use_time=0
                for cache_city,time in cache.items():
                    if cache_city in cities:
                        if time>recent_use_time:
                            recent_use_time=time
                            remove_cache_city=cache_city

                if cacheSize>0:
                    cache.pop(remove_cache_city)
                    cache[city]=len(cities)-idx

    return answer

print(solution(3,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(0,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))