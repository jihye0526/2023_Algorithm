// 다른 사람 풀이
function solution(k, d) {
    let answer = 0;
    
    for(let a=0; a<=d; a=a+k){
        let b = parseInt(((d**2) - (a**2)) ** 0.5)
        
        answer += parseInt(b/k)+1;
    }
    
    return answer;
}

console.log(solution(2, 4))
console.log(solution(1, 5))