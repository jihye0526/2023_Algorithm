# 내 풀이
def solution(brown, yellow):
    total = brown+yellow
    
    arr = [i for i in range(2, int(total**0.5)+1) if total % i == 0]
    
    for i in arr:
        x, y = int(total/i), i
    
        if ((x*2) + (y*2) - 4) == brown:
            return [x, y]
        
# 다른 사람 풀이
def solution2(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
        
print(solution(10, 2))
print(solution(8, 1))
print(solution2(24, 24))