# 내 풀이
def solution(dartResult):
    num = -1
    arr = []
    
    for i in dartResult:
        if i in '012345678910':
            # num이 0 ~ 9 일 때
            if num == -1: num = int(i)
            # num == 10 일 때
            else: num = int(str(num) + i)
        elif i in 'SDT':
            if i == 'S': num
            elif i == 'D': num **= 2
            elif i == 'T': num **= 3
            arr.append(num)
            # arr에 append한 상태를 나타냄. 10일 경우 for문을 돌며 1, 0 이 분리 되기 때문에 로직 추가
            num = -1
        elif i in '*#':
            if len(arr) == 1 and i == '*': 
                arr[-1] *= 2
            elif i == '*':
                arr[-1] *= 2
                arr[-2] *= 2
            elif i == '#': 
                arr[-1] *= -1
    
    return sum(arr)

# 다른 사람 풀이
import re

def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# 다른 사람 풀이2
def solution3(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i])**dart[d])
        if d == "*":
            scores[-2:] = [x*2 for x in scores[-2:]]
        if d == "#":
            scores[-1] = (-1)*scores[-1]
        if not (d.isnumeric()):
            n = i+1

    return sum(scores)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution2("1S*2T*3S"))
print(solution2("1D#2S*3S"))
print(solution2("1T2D3D#"))
print(solution3("1D2S3T*"))