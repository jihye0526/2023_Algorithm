# 다른 사람 풀이 1
from collections import Counter

def solution(topping):
    answer = 0
    baseSet = set(topping)
    compareSet = set()
    counter = Counter(topping)
    
    for i in topping:
        counter[i] -= 1
        
        if counter[i] == 0:
            baseSet.remove(i)
        
        compareSet.add(i)
        
        if len(baseSet) == len(compareSet):
            answer += 1
            
    return answer

def solution2(topping):
    answer = 0

    l, r = 0, len(topping)
    idx1 = 0
    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))
        if left < right:
            l = m + 1
        elif left >= right:
            idx1 = m
            r = m - 1

    l, r = 0, len(topping)
    idx2 = 0
    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))
        if left <= right:
            idx2 = m
            l = m + 1
        elif left > right:
            r = m - 1

    answer = max(idx2 - idx1 + 1, 0)

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution2([1, 2, 3, 1, 4]))