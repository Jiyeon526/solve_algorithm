def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.upper()
        if city not in cache:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
        
    return answer