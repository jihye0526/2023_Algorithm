# 내 코드
def solution(s, n):
    answer = ''
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in s:
        # 공백일땐 그대로 출력
        if i == ' ':
            answer += ' '
            
        # 대문자 일 때    
        elif i in big:
            # 현재 문자의 index를 찾고 n을 더함
            idx = big.index(i)+n
            
            # idx가 big의 길이보다 크면
            if idx >= len(big)-1:
                idx -= len(big)
                
            answer += big[idx]
            
        # 소문자 일 때    
        elif i in small:
            # 현재 문자의 index를 찾고 n을 더함
            idx = small.index(i)+n
            
            # idx가 small의 길이보다 크면
            if idx >= len(small)-1:
                idx -= len(small)
                
            answer += small[idx]
            
    return answer

def solution2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

print(solution("AB", 1))
print(solution("z", 1))
print(solution2("a B z", 4))