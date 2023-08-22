# 내 풀이
from collections import deque

def solution(s):
    answer = 0
    q = deque(s)
    temp = []

    for _ in range(len(q)):
        for i in range(len(q)):
            if q[i] in '{[(':
                temp.append(q[i])
            elif len(temp) != 0 and q[i] in ')]}':
                if temp[-1] == '[' and q[i] == ']':
                    temp.pop()
                elif temp[-1] == '{' and q[i] == '}':
                    temp.pop()
                elif temp[-1] == '(' and q[i] == ')':
                    temp.pop()
                else:
                    break
            elif len(temp) == 0 and q[i] in ')]}':
                break

            if i == (len(q)-1) and len(temp) == 0: answer += 1
        
        x = q.popleft()
        q.append(x)
    
    return answer

# 다른 사람 풀이 1
from collections import deque

def check(s):
    while True:
        if "()" in s: s=s.replace("()","")
        elif "{}" in s: s=s.replace("{}","")
        elif "[]" in s: s=s.replace("[]","")
        else: return False if s else True       

def solution2(s):
    ans = 0
    que = deque(s)

    for _ in range(len(s)):
        if check(''.join(que)): ans+=1
        que.rotate(-1)
    return ans

# 다른 사람 풀이 2
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

def solution3(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer

print(solution("[](){}"))
print(solution2("}]()[{"))
print(solution2("[)(]"))
print(solution3("}}}"))