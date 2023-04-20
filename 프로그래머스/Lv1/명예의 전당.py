def solution(k, score):
    answer = []
    result = []
    
    for i in score:
        answer.append(i)
        if len(answer) > k:
            answer.remove(min(answer))
            
        result.append(min(answer))
        
    return result

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))