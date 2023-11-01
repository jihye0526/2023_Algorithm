# 다른 사람 풀이
def solution(n):
    dp = [0 for _ in range(n)]
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[n-1]

def solution2(n):
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, (a + b) % 1000000007
    return b

print(solution(4))
print(solution2(4))