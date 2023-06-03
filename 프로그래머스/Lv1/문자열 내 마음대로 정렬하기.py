# 내 코드
def solution(strings, n):
    # lambda를 이용하여 각 원소의 n번째를 key로 정렬. 우선순위가 동일하면 x를 기준으로 정렬
    return sorted(strings, key=lambda x : (x[n], x))

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))