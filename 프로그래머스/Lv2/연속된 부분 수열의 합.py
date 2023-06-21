# 내 풀이
def solution(sequence, k):
    answer = []
    sum = 0
    start, end = 0, 0
    length = len(sequence)
    
    for i, v in enumerate(sequence):
        sum += v
        end = i
        
        while sum > k:
            sum -= sequence[start]
            start += 1
            
        if sum == k and (end - start < length):
            answer = [start, end]
            length = end - start
        
    return answer

print(solution([1,2,3,4,5], 7))
print(solution([1,1,1,2,3,4,5], 5))
print(solution([2,2,2,2,2], 6))