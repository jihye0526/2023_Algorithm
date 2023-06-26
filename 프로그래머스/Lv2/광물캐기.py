# 내 풀이
import math

def solution(picks, minerals):
    answer = 0
    points = [25 if mineral == 'diamond' else 5 if mineral == 'iron' else 1 for mineral in minerals]
    arr = []
        
    for i in range(0, min(len(minerals), sum(picks)*5), 5):
        arr.append(points[i:i+5])
        
    arr.sort(key=lambda x: sum(x), reverse=True)
    power = -1
    
    for i in range(len(arr)):
        if picks[0] > 0:
            power = 25
            picks[0] -= 1
        elif picks[1] > 0:
            power = 5
            picks[1] -= 1
        elif picks[2] > 0:
            power = 1
            picks[2] -= 1
        
        for j in range(len(arr[i])):
            answer += math.ceil(arr[i][j] / power)
        
        if sum(picks) == 0: break
        
    return answer

# 다른 사람 풀이
def solution2(picks, minerals):
    def solve(picks, minerals, fatigue):
        if sum(picks) == 0 or len(minerals) == 0:
            return fatigue
        result = [float('inf')]
        for i, fatigues in enumerate(({"diamond": 1, "iron": 1, "stone": 1},
                                      {"diamond": 5, "iron": 1, "stone": 1},
                                      {"diamond": 25, "iron": 5, "stone": 1},)):
            if picks[i] > 0:
                temp_picks = picks.copy()
                temp_picks[i] -= 1
                result.append(
                    solve(temp_picks, minerals[5:], fatigue + sum(fatigues[mineral] for mineral in minerals[:5])))
        return min(result)

    return solve(picks, minerals, 0)

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))
print(solution2([0, 1, 0], ["diamond", "iron", "iron", "iron", "iron", "diamond", "diamond", "iron", "iron", "iron"]))