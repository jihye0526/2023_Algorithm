// 내 풀이
function solution(x) {
    let num = 0;
    x = x.toString();
    
    for(let i=0; i<x.length;i++){
        num += Number(x[i]);
    }
    return x % num === 0 ? true : false;
}

// 다른 사람 풀이
function solution2(x){
    return !(x % (x+"").split("").reduce((a, c) => +a + +c));
}

console.log(solution(10));
console.log(solution(12));
console.log(solution2(11));
console.log(solution2(13));