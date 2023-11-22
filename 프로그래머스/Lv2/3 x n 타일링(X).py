# 다른 사람 풀이
def solution(n):
    answer = 0
    dp = [0 for i in range(n+1)]
    dp[2] = 3

    for i in range(3, n+1):
        if i % 2 == 0:
            dp[i] = (dp[i-2] * 3 + sum(dp[2:i-2])*2 + 2) % 1000000007
            
    return dp[n]

print(solution(4))
print(solution(6))
print(solution(8))