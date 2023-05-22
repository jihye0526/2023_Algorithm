# 내 코드
def solution(x):
    answer = True
    num = 0

    for i in str(x):
        num += int(i)

    if x % num == 0: 
        answer = True 
    else: 
        answer = False

    return answer

# 다른 사람 코드
def solution2(x):
    return x%sum([int(i) for i in str(x)]) == 0

print(solution(10))
print(solution(12))
print(solution2(11))
print(solution2(13))