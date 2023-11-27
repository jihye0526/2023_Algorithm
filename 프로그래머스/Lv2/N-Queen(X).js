// 다른 사람 풀이
function solution(n) {
    let answer = 0;
    
    for(let i=0; i<n; i++){
        const board = new Array(n).fill(0);
        // 체스판의 첫번째 세로라인 중 i칸에 퀸을 배치
        board[0] = i; 
        // 배치가 완료된 체스판과 현재 세로라인인 0을 dfs 함수에 전달
        dfs(board, 0); 
    }
    
    function dfs(board, row){
        if(n-1 === row) answer++;
        else{
            for(let i=0; i<n; i++){
                // 다음 라인에 퀸 배치
                board[row+1] = i; 
                // isValid 라는 함수를 통해 해당 위치 퀸이 유효한지 검사
                // 유효하다면 다음위치 계속 탐색
                if(isValid(board, row+1)) dfs(board, row+1);
            }
        }
    }
    
    function isValid(board, row){
        // 현재라인과 이전 라인을 검사
        for(let i=0; i<row; i++){
            // 같은 라인에 있는 경우 배치 불가
            if(board[i] === board[row]) return false;
            // 대각 라인에 있는 경우 배치 불가
            if(Math.abs(row-i) === Math.abs(board[row]-board[i])) return false;
        }
        
        return true;
    }
    
    return answer;
}

console.log(solution(4))