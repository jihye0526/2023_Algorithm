// 내 풀이
function solution(x, n) {
    let answer = [];
    
    for(let i=1; i<=n; i++){
        answer.push(x*i);
    }
    
    return answer;
}

// 다른 사람 풀이
function solution2(x, n){
    return Array(n).fill(x).map((a, b) => a * (b+1));
}

console.log(solution(2, 5));
console.log(solution2(4, 3));
console.log(solution2(-4, 2));