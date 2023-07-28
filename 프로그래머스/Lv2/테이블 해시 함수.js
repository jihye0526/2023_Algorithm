// 내 풀이
function solution(data, col, row_begin, row_end) {
    const arr = [];
    data.sort((a, b) => a[col-1] - b[col-1] || b[0] - a[0]);
    
    for(let i=row_begin-1; i<row_end; i++){
        let temp = 0;
        for(let j=0; j<data[i].length; j++){
            temp += data[i][j] % (i+1);
        }
        arr.push(temp);
    }
    
    return arr.reduce((a, c) => a ^ c , 0);
}

console.log(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]]));