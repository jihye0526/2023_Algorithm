// 내 풀이
function solution(numbers) {
    let answer = 0;
    
    [0,1,2,3,4,5,6,7,8,9].reduce((a,b) => {
        numbers.indexOf(b) == -1 ? answer += b : 0
    }, answer);
    return answer;
}

// 다른 사람 풀이
function solution2(numbers) {
    return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}

console.log(solution([1,2,3,4,6,7,8,0]));
console.log(solution2([5,8,4,0,6,7,9]));