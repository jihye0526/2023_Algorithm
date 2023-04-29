# 내 풀이
def solution(X, Y):
    answer = ''
    number = set(X) # 0 ~ 9까지 for문을 돌리지 않고 들어가 있는 문자의 길이만큼만 돌게 하기 위함
    dict = {}

    for i in number:
        if i in X and i in Y:
            dict[i] = min(X.count(i), Y.count(i))
            
    dict = sorted(dict.items(), key = lambda item: item[0], reverse = True)
    
    for i in dict:
        answer += i[0]*i[1]
    
    if answer == "":
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"
    
    return answer

# 다른사람의 풀이
def solution2(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer

print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution2("100", "123450"))
print(solution2("12321", "42531"))
print(solution2("5525", "1255"))