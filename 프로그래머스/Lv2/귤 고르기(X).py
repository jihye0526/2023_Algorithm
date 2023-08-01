# 다른 사람 풀이 1
def solution(k, tangerine):
    answer = 0
    dict = {}
    
    # count함수를 사용하면 시관초과뜸 O(n^2)
    for i in tangerine:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    
    for i in dict:
        if k > 0:
            k -= i[1]
            answer += 1
        else:
            break
    
    return answer

# 다른 사람 풀이 2
from collections import Counter

def solution2(k, tangerine):
    answer = 0
    # 시간 복잡도 O(n)
    cnt = Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer


# 다른 사람 풀이 3
def solution3(k, tangerine):
    counter = Counter(tangerine)
    tangerine.sort(key = lambda t: (-counter[t], t))
    return len(set(tangerine[:k]))

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution2(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution3(2, [1, 1, 1, 1, 2, 2, 2, 3]))