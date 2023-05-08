# 내 풀이
def solution(absolutes, signs):
    return sum([x * (1 if y else -1) for x, y in zip(absolutes, signs)])

# 다른 사람 풀이
def solution2(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

print(solution([4,7,12], [True,False,True]));
print(solution2([1,2,3], [False,False,True]));