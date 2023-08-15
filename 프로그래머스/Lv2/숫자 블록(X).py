# 다른 사람 풀이
def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        min_num = 1
        max_num = 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                #  1부터 10,000,000까지의 숫자가 적힌 블록
                if i // j <= 10000000:
                    min_num = j
                    answer.append(i // j)
                    break
                else:
                    max_num = j
                    
        if i == 1:
            answer.append(0)
        elif min_num == 1:
            answer.append(max_num)
    return answer

print(1, 10)
print(5, 20)
print(solution(1000000000-5000, 1000000000))