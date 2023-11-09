def solution(n, wires):
    dp = [1 for i in range(n)]

    wires.sort(key=lambda x:x[0])

    for i in range(1, n):
        for j in range(i):
            if wires[i][1] > wires[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
        print(dp)
    return n - max(dp)

print(solution(8, [[1,8], [3,9], [2,2], [4,1], [6,4], [10,10], [9,7], [7,6]]))