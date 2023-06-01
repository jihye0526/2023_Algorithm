# 내 풀이
def solution(n):
    answer = 0
    
    # 1과 2의 배수는 소수가 아니므로 3부터 홀수만 체크
    for i in range(3, n+1, 2):
        cnt = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0: 
                cnt += 1
                break
        
        if cnt == 0: answer += 1
        
    return answer+1 # 소수 2를 마지막에 더해줌

# 다른 사람 풀이
def solution2(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

print(solution(10))
print(solution2(5))