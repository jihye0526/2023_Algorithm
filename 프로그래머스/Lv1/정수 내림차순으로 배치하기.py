# 내 코드
def solution(n):
    return int(''.join(list(sorted(str(n), reverse=True))))

print(solution(118372))