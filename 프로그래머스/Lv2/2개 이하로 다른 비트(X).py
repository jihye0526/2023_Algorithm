# 다른 사람 풀이 1
def solution(numbers):
    answer = []

    for number in numbers:
        answer.append(((number ^ (number+1)) >> 2) +number +1)

    return answer

# 다른 사람 풀이 2
def solution2(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            bin_number = bin(number).replace("b", "")
            idx = bin_number.rindex("0")
            answer.append(int(bin_number[:idx] + "10" + bin_number[idx+2:], 2))

    return answer

print(solution([2,7]))
print(solution2([2,7]))