# 내 코드
def solution(a, b):
    if a > b : a, b = b, a
    
    return sum([i for i in range(a, b+1)])

# 다른 사람 코드
def solution2(a, b):
    return (abs(a-b)+1)*(a+b)//2

print(solution(3, 5))
print(solution(3, 3))
print(solution2(5, 3))