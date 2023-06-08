# 내 풀이
def solution(s):
    answer = ""
    
    if len(s) % 2 == 0 : 
        answer = s[len(s)//2-1:len(s)//2+1] 
    else : 
        answer = s[len(s)//2]
        
    return answer

def solution2(s):
    return str[(len(s)-1)//2 : len(s)//2 + 1]

print(solution("abcde"))
print(solution2("qwer"))