// 내 풀이
function solution(left, right) {
    let answer = 0;
    
    for(let i=left; i<right+1; i++){
        if(Number.isInteger(Math.sqrt(i))){
           answer -= i;
        }else{
            answer += i;
        }
    }
    
    return answer;
}

console.log(solution(13,17));
console.log(solution(24,27));