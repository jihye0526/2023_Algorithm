# 내 풀이
import math

def solution(n,a,b):
    answer = 0

    while a != b:
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2) # a, b = math.ceil(a/2), math.ceil(b/2)로 변경 가능
        
        # while 조건문이 있어서 필요없음,,ㅠ
        if a == b:
            break
    
    return answer

# 다른 사람 풀이
def solution2(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer