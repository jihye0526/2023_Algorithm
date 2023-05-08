// 내 풀이
function solution(absolutes, signs) {
    let answer = 0;
    
    for(let i=0; i<signs.length; i++){
        if(signs[i]){
            answer += absolutes[i];
        }else{
            answer -= absolutes[i];
        }
    }
    return answer;
}

// 다른 사람 풀이
function solution2(absolutes, signs){
    return absolutes.reduce((a, c, i) => a + c * (signs[i] ? 1 : -1), 0);
}

console.log(solution([4,7,12], [true,false,true]));
console.log(solution2([1,2,3], [false,false,true]));