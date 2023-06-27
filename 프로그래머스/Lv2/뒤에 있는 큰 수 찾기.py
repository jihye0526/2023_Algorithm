# 내 풀이(시간 초과)
def solution(numbers):
    answer = []
    numbers.reverse()
    
    while numbers:
        num = numbers.pop()
        
        temp = [i for i in numbers if i > num]
        
        if len(temp):
            answer.append(temp[-1])
        else:
            answer.append(-1)
            
    return answer

# 다른 사람 풀이
def solution2(numbers):
    answer = [-1]*(len(numbers))
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer

print(solution([2, 3, 3, 5]))
print(solution2([9, 1, 5, 3, 6, 2]))