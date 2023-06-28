# 내 풀이
def solution(s):
    stack = []

    for i in s:
        stack.append(i)
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    
    if len(stack) == 0:
        return 1
    else: 
        return 0
    
# 다른 사람 풀이
def solution2(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)

print(solution("baabaa"))
print(solution2("cdcd"))