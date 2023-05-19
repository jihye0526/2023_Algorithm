// 내 풀이
function solution(arr1, arr2) {
    let result = [];
    
    for(let i=0; i<arr1.length; i++){
        let answer = [];
        for(let j=0; j<arr1[i].length; j++){
            answer.push(arr1[i][j]+arr2[i][j]);
        }
        result.push(answer);
    }
    
    return result;
}

// 다른 사람 풀이
function solution2(A,B){
    return A.map((arr1, idx1) => arr1.map((val, idx2) => val+B[idx1][idx2]));
}

console.log(solution([[1,2],[2,3]],[[3,4],[5,6]]));
console.log(solution2([[1],[2]],[[3],[4]]));