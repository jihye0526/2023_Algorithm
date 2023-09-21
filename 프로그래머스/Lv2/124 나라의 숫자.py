# 내 풀이
def solution(n):
    answer = ''
    a, b = (n-1)//3, (n-1)%3
    
    while True:
        if b == 0: answer += '1'
        elif b == 1: answer += '2'
        elif b == 2: answer += '4'
        
        if a == 1: answer += '1'
        elif a == 2: answer += '2'
        elif a == 3: answer += '4'
        if a < 4: break
        a, b = (a-1)//3, (a-1)%3
        
    temp = list(map(str, answer))
    temp.reverse()
    return ''.join(temp)

def solution2(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

print(solution(1))
print(solution(2))
print(solution2(3))
print(solution2(4))
print(solution(18))