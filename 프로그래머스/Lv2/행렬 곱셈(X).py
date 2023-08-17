# 다른 사람 풀이 1
def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)): 
        for j in range(len(arr2[0])): 
            for k in range(len(arr1[0])): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

# 다른 사람 풀이 2
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(productMatrix([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))