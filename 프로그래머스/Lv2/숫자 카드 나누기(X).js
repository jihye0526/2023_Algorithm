// 다른 사람 풀이 1
function gcd(a, b){
    let remainder = a % b;
    return remainder === 0? b : gcd(b, remainder);
}

function solution(arrayA, arrayB) {
    var answer = [];
    
    let n1 = arrayA.reduce((a, c) => gcd(a, c));
    let n2 = arrayB.reduce((a, c) => gcd(a, c));
    
    if(arrayA.every((e) => e%n2 !== 0)) answer.push(n2);
    if(arrayB.every((e) => e%n1 !== 0)) answer.push(n1);
    
    return answer.length === 0 ? 0 : Math.max(...answer);
}

// 다른 사람 풀이 2
function solution2(arrayA, arrayB) {
    const aResult = getAnswer(arrayA, arrayB)
    const bResult = getAnswer(arrayB, arrayA)

    return aResult > bResult ? aResult : bResult
}

function getAnswer (A, B) {
    A.sort((a, b) => a - b)
    for (let i = A[0]; i > 1; i--) {
        if (A.every(a => a % i === 0) && !B.some(b => b % i === 0)) return i
    }
    return 0
}

console.log(solution([10, 17], [5, 20]));
console.log(solution2([10, 20], [5, 17]));
console.log(solution2([14, 35, 119], [18, 30, 102]));