# 내 풀이
def solution(n):
    # n진수  → 10진수 : int(string, base)
    # 10진수  → 2, 8, 16진수 bin(), oct(), hex() 함수를 지원
    answer = ""
    i = 1

    while n >= 3**i:
        i += 1

    for j in range(i-1, -1, -1):
        for k in range(2, -1, -1):
            if 3**j*k <= n : 
                answer += str(k)
                n -= 3**j*k
                break

    answer = answer[::-1]

    return int(answer, 3)

# 다른 사람 풀이
def solution2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

print(solution(45))
print(solution2(125))