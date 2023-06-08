# 내 풀이
def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    
    
    return answer

def solution2(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

print(solution([1,1,3,3,0,1,1]))
print(solution2([4,4,4,3,3]))