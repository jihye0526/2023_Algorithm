# 다른 사람 풀이 1
from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1

# 다른 사람 풀이 2
solution2 = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1


# 다른 사람 풀이 3
def solution3(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer

print(solution("AAAAE"))
print(solution2("AAAE"))
print(solution3("I"))
print(solution("EIO"))