# 내 풀이
def solution(want, number, discount):
    answer = 0
    total = sum(number)
    arr = []
    
    for i, v in enumerate(want):
        for j in range(number[i]):
            arr.append(v)

    arr.sort()
    
    for i in range(len(discount)):
        temp = discount[i:i+total]
        temp.sort()
        if arr == temp: answer += 1
    
    return answer

# 다른 사람 풀이
from collections import Counter
def solution2(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1]))
print(solution2(["apple"], [10]))