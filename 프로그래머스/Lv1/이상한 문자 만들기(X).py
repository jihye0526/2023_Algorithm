def solution(s):
    answer = ''
    # split(' ')과 split의 차이
    # 'hello  jihye' 의 경우 split(' ')을 하게 되면 ['hello', '', 'jihye'] 이지만 split()을 하게 되면 ['hello', 'jihye']임
    arr = s.split(' ')
    print(arr)
    for word in arr:
        for i in range(len(word)):
            if i % 2 == 0 : answer += word[i].upper()
            else : answer += word[i].lower()
        answer += ' '

    return answer[0:-1] # rstrip을 사용하고 싶었는데 계속 실패가 뜨고 [0:-1]을 사용하면 성공을 함. strip()은 재귀적으로 호출,,,? 'abc'를 인자로 주면 'a'를 제거하고 'b'를 제거하고 'c'를 제거함. 하지만 공백이 무슨 문제인지는 모르겠음

print(solution("try hello world"))