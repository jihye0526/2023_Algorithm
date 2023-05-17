# 내 풀이
def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if(decimal(nums[i]+nums[j]+nums[k]) == 0):
                    answer += 1

    return answer

def decimal(num):
    cnt = 0
    
    for i in range(2, num):
        if num % i == 0:
            cnt += 1
    
    return cnt

# 다른 사람 풀이
def solution2(nums):
    from itertools import combinations as cb 
    answer = 0
    for a in cb(nums, 3): # combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합 뽑기
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

print(solution([1,2,3,4]))
print(solution2([1,2,7,6,4]))