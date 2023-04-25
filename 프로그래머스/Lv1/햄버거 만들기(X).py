def solution(ingredient):
    answer = 0
    arr = []
    
    for i in ingredient:
        arr.append(i)
        
        if arr[-4:] == [1, 2, 3, 1]:
            answer += 1
            
            for j in range(4):
                arr.pop();
        
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
