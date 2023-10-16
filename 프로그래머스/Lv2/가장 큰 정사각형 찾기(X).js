// 다른 사람 풀이
function solution(board)
{
    let answer = 0;
    let row = board.length;
    let col = board[0].length;
    
    if(row <= 1 || col <= 1) return 1;
    
    for(let i=1; i<row; i++){
        for(let j=1; j<col; j++){
            if(board[i][j] > 0){
                board[i][j] = Math.min(board[i][j-1], board[i-1][j-1], board[i-1][j]) + 1;
            
                answer = Math.max(board[i][j], answer);
            }
        }
    }

    return answer**2;
}

console.log(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
console.log(solution([[0,0,1,1],[1,1,1,1]]))