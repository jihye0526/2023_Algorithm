# 내 풀이
def solution(nums):
    answer = 0
    
    if(len(set(nums)) > int(len(nums)/2)):
        answer = int(len(nums)/2)
    else:
        answer = len(set(nums))
                     
    return answer

# 다른 사람 풀이
def solution2(ls):
    return min(len(ls)/2, len(set(ls)))

print(solution([3,1,2,3]))
print(solution2([3,3,3,2,2,4]))
print(solution2([3,3,3,2,2,2]))