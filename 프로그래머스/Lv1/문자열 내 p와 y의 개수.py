# 내 풀이
def solution(s):
    s = s.lower()
    p_cnt = s.count('p')
    y_cnt = s.count('y')

    return p_cnt == y_cnt

# 다른 사람 풀이
def soolution2(s):
    return s.lower().count('p') == s.lower().count('y')


print(solution("pPoooyY"))
print(soolution2("Pyy"))