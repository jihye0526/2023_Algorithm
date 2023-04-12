def solution(s):
    answer = []
    dict = {}
    
    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = i
            answer.append(-1)
        else:
            answer.append(len(s[dict[s[i]]:i]))
            dict[s[i]] = i
            
    return answer

print(solution("banana"))
print(solution("foobar"))
