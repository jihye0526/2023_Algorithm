// 내 풀이
function solution(n) {
    let answer = 0;
    
    for(let i=0; i<=n**0.5; i++){
        if(n%i === 0){
            i*i === n ? answer += i : answer += i + n/i;
        }
    }
    return answer;
}

console.log(solution(12));
console.log(solution(5));