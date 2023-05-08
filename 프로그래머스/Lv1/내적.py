# 내 풀이
def solution(a, b):
    answer = 0
    
    for i in range(len(a)): 
        answer += a[i] * b[i]
        
    return answer

# 다른 사람 풀이
def solution2(a, b):
    return sum([x*y for x, y in zip(a,b)]) # zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환

print(solution([1,2,3,4], [-3,-1,0,2]));
print(solution2([-1,0,1], [1,0,-1]));