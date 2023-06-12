# 내 풀이
def solution(board, moves):
    answer = 0
    # 뽑은 인형 담을 배열
    arr = []
    
    for i in moves:
        for j, v in enumerate(list(zip(*board))[i-1]): # idx와 value값을 담음
            if v != 0:
                # 제일 위에 인형을 뽑아서 해당 위치의 값을 0으로 바꿈
                board[j][i-1] = 0

                if len(arr) != 0 and arr[-1] == v:
                    arr.pop()
                    answer += 2
                else:
                    arr.append(v)
                break
    
    return answer

# 다른 사람 풀이
def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
print(solution2([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))