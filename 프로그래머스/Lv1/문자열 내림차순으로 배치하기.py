# 내 코드
def solution(s):
    arr = [i for i in s]
    arr.sort(reverse=True)
        
    return ''.join(arr)

# 다른 사람 코드
def solution2(s):
    return ''.join(sorted(s, reverse=True))

print(solution("Zbcdefg"))
print(solution2("Zbcdefg"))