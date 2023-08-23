# 내 풀이
from collections import Counter

def solution(s):
    result = s
    x, y = 0, 0
    
    while result != "1":
        cnt = Counter(result)
        
        x += 1
        y += cnt["0"]
        
        result = bin(cnt["1"]).replace("0b", "")
    
    return [x, y]

# 다른 사람 풀이
def solution2(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

print(solution("110010101001"))
print(solution2("01110"))
print(solution2("1111111"))