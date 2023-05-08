# 내 풀이
def solution(lottos, win_nums):
    answer = []
    best = 0
    worst = 0
    
    for i in lottos:
        if i in win_nums: 
            best += 1
            worst += 1
        elif i == 0:
            best += 1
        
    if best == 0 : best = 1
    if worst == 0: worst = 1
    
    answer = [7-best, 7-worst]
    
    return answer

# 다른 사람 풀이
def solution2(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return [rank[cnt_0 + ans],rank[ans]]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution2([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution2([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))