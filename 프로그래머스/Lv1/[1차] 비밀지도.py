# 내 풀이
def solution(n, arr1, arr2):
    answer = [bin(i|j) for i, j in zip(arr1, arr2)]
    return [i.replace('0b', '').rjust(n, '0').replace('1', '#').replace('0', ' ') for i in answer]

# 다른 사람 풀이
solution2 = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution2(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))