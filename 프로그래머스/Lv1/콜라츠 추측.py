# 내 풀이
def solution(num):
    answer = -1
    
    if num != 1:
        for i in range(1, 501):
            if num % 2 == 0:
                num = int(num / 2)
            else:
                num = (num * 3) + 1

            if num == 1: 
                answer = i
                break
    else:
        answer = 0
            
    return answer

# 다른 사람 풀이
def solution2(num):
    for i in range(500):
        if i == 0 and num == 1: return 0
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1

print(solution(6))
print(solution2(16))
print(solution2(626331))