# 내 코드
def solution(s):
    answer = True
    
    if len(s) != 4 and len(s) != 6: return False
    
    for i in s:
        if i not in '0123456789':
            answer = False
        
    return answer

# 다른 사람 코드
def solution2(s):
    return s.isdigit() and len(s) in [4,6]

print(solution("a234"))
print(solution2("1234"))