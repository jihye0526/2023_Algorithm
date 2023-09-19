// 내 풀이
function solution(n, k) {
    let answer = 0;
    let digitalNum = n.toString(k);
    let arr = digitalNum.split("0");
    
    arr.map((i) => {
        if(i > 1) answer += sosu(i);
    });
    
    return answer;
}

function sosu(num){
    let cnt = 0;
    
    for(i=2; i<parseInt(num**0.5)+1; i++){
        if(num % i === 0) cnt++;
    }
    
    return cnt === 0 ? 1 : 0;
}

// 다른 사람 풀이
function isPrime(num){
    if(!num || num===1) return false;
    for(let i=2; i<=+Math.sqrt(num); i++){
        if(num%i===0) return false;
    }
    return true;
}

function solution2(n, k) {    
    // k진법으로 나눈 후 split
    const candidates = n.toString(k).split('0');
    // 소수 개수 세기
    return candidates.filter(v=>isPrime(+v)).length;
}

console.log(solution(437674, 3))
console.log(solution(110011, 10))
console.log(solution2(930909,10))
