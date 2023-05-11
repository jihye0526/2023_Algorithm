// 내 풀이
function solution(answers) {
    let answer = [0,0,0];
    let result = [];
    let first = [1,2,3,4,5];
    let second = [2,1,2,3,2,4,2,5];
    let third = [3,3,1,1,2,2,4,4,5,5];
    
    for(let i=0; i<answers.length; i++){
        first[i%first.length] === answers[i] ? answer[0] += 1 : 0;
        second[i%second.length] === answers[i] ? answer[1] += 1 : 0;
        third[i%third.length] === answers[i] ? answer[2] += 1 : 0;
    }
    
    let cnt = Math.max(...answer);
    
    for(let i=0; i<answer.length; i++){
        if(answer[i] === cnt){
            result.push(i+1);
        }
    }
    
    return result;
}

console.log(solution([1,2,3,4,5]));
console.log(solution([1,3,2,4,2]));