# 다른 사람 풀이 1
def solution(plans):
    answer = []
    stack = []
    
    plans.sort(key=lambda x:x[1])
    
    for plan in plans:
        h, m = map(int, plan[1].split(":"))
        plan[1] = h*60 + m
        plan[2] = int(plan[2])
    
    for i in range(len(plans)): # 시간안에 과제를 못 끝낼경우, 끝낼경우
        if i == len(plans)-1: # 마지막 과제에 도달했을 경우
            answer.append(plans[i][0])
            for i in range(-1, -len(stack)-1, -1):
                answer.append(stack[i][0])
            break
        extra = plans[i+1][1] - (plans[i][1]+plans[i][2]) # 다음과제시간 - (현재 과제시간 + 과제 진행시간)
        
        if extra >= 0: # 시간 안에 끝낼수 있는경우 추가과제 할수 있으면 한다
            answer.append(plans[i][0])
            while stack:
                if stack[-1][1] <= extra: # 여분의 시간이 스택에 남은 시간보다 클 경우
                    k = stack.pop()
                    answer.append(k[0]) # 과제이름
                    extra -= k[1]
                
                else:
                    stack[-1][1] -= extra
                    break
        else: # 다음 과제시간까지 못 끝낸경우
            stack.append([plans[i][0], -extra])
    
    return answer

# 다른 사람 풀이 2
def solution2(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]	))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]	))
print(solution2([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]	))