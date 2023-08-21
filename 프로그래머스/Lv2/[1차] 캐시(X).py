# 내 풀이(75점)
def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]
    for city in cities:
        cacheCities = [x[0] for x in cache]
        
        if city in cacheCities:
            answer += 1
            idx = cacheCities.index(city)
            cache[idx][1] += 1
        elif len(cache) < cacheSize and city not in cache:
            cache.append([city, 1])
            answer += 5
        elif len(cache) >= cacheSize and city not in cache:
            sorted(cache, key=lambda a: a[1])
            if cache: cache = cache[1:]
            if len(cache) < cacheSize: cache.append([city, 1])
            answer += 5
        
    return answer

# 내 풀이 수정

def solution_eidt(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]
    
    for city in cities:
        if cacheSize == 0:
            return len(cities)*5
        else:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.append(city)
            else:
                answer += 5
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
    return answer

# 다른 사람 풀이
def solution2(cacheSize, cities):
    answer = 0
    i = 0              # 초기 캐시 인덱스
    cache = []
    if cacheSize == 0:                # 캐시 사이즈가 0이면,
        return len(cities)*5
    for c in cities:              
        city = c.upper()              # city 이름 대문자 통일
        if city in cache:             # 캐시에 이미 있는 city의 경우
            cache.remove(city)        # 해당 city 캐시에서 위치 재조정
            cache.append(city)
            answer += 1
        else:                         # 캐시에 없는 city의 경우
            answer += 5 
            if i < cacheSize:         # 아직 캐시에 빈 공간이 있다면
                cache.append(city)
                i += 1
            else:                     # 캐시에 빈 공간이 없다면
                cache.pop(0)          # 캐시 내부 city 하나 교체
                cache.append(city)

    return answer

# 다른 사람 풀이 2
import collections

def solution3(cacheSize, cities):
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution2(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution2(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution3(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution3(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))