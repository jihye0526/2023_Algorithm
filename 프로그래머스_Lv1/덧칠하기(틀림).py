def solution(n, m, section):
    answer = painted = 0
    
    for s in section:
        if s >= painted:
            painted = s + m
            answer += 1
    
    return answer

print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))