# 내 풀이
import math

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        num = math.sqrt(i)
        if int(num) == num:
            answer -= i
        else:
            answer += i
        
    return answer

# 다른 사람 풀이
def solution2(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13,17));
print(solution(24,27));