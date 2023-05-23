# 내 풀이
def solution(n):
    answer = [int(i) for i in str(n)]
    answer.reverse()
    
    return answer

# 다른 사람 풀이
def solution2(n):
    return list(map(int, reversed(str(n))))

print(solution(12345))