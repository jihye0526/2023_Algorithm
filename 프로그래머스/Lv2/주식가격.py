# 내 풀이
def solution(prices):
    answer = []
    
    for idx, price in enumerate(prices):
        cnt = 0
        for i in range(idx+1, len(prices)):
            cnt += 1
            if price > prices[i]:
                answer.append(cnt)
                break
                
            if (i+1) == len(prices):
                answer.append(cnt)
                
    answer.append(0)
    
    return answer

# 다른 사람 풀이
def solution2(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

print(solution([1, 2, 3, 2, 3]))
print(solution2([1, 2, 3, 2, 3]))