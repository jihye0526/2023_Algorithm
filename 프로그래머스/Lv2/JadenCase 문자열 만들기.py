# 내 풀이
import re

def solution(s):
    arr = s.split(' ')
    p = re.compile('^[a-zA-Z]')
    
    for i, val in enumerate(arr):
        arr[i] = val.lower()
        
        if p.search(val):
            # capitalize() : 문자열에서 맨 첫 글자를 대문자로 변환
            # title() : 문자열에서 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 나누어져 있는 영단어들의 첫 글자를 모두 대문자로 변환시킨다.
            arr[i] = arr[i].capitalize() 
            
    return ' '.join(arr)

print(solution("3people unFollowed me"))
print(solution("3PeoPle unFollowed me"))
print(solution("for the last week"))