# 다른 사람 풀이
def solution(targets):
    answer = 0
    point = -1
    
    targets.sort(key=lambda x : (x[1], x[0]))
    
    for target in targets:
        if target[0] >= point:
            answer += 1
            point = target[1]
        
    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))