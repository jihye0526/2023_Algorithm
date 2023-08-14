# 다른 사람 풀이 1
def solution(order):
    assist = []
    i = 1
    cnt = 0 
    while i != len(order)+1:
        assist.append(i)
        while assist and assist[-1] == order[cnt]:
            cnt += 1
            assist.pop()
            
        i += 1
    return cnt

# 다른 사람 풀이 2
def solution2(order):
    stacks = []
    N = len(order)
    i = 1
    idx = 0
    while i < N+1:
        stacks.append(i)
        while stacks[-1] == order[idx]:
            idx += 1
            stacks.pop()
            if len(stacks) == 0:
                break
        i += 1


    return idx

print(solution([4, 3, 1, 2, 5]))
print(solution2([5, 4, 3, 2, 1]))