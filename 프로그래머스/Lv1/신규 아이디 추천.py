# 내 코드
import re

def solution(new_id):
    answer = ''
    
    # step 1
    answer = new_id.lower()
    # step 2
    arr = [i for i in answer if i in '0123456789abcdefghijklmnopqrstuvwxyz-_.']
    answer = ''.join(arr)
    # step 3
    answer = re.sub('\.+', '.', answer)	
    # step 4
    answer = answer.strip('.')
    # step 5
    if len(answer) == 0: answer = 'a'
    # step6
    if len(answer) >= 16: answer = answer[:15]
    answer = answer.rstrip('.')
    # step 7
    if len(answer) <= 2: answer = answer.ljust(3, answer[-1])
    
    return answer

def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution2("=.="))
print(solution2("123_.def"))
print(solution2("abcdefghijklmn.p"))