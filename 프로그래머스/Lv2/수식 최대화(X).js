// 다른 사람 풀이
function solution(expression) {
    let answer = [];
    const ops = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '+', '-'],
        ['*', '-', '+']
    ];
    
    for(let op of ops){
        const temp = expression.split(/([\D])/);
        for(let i of op){
            while(temp.includes(i)){
                const idx = temp.indexOf(i);
                temp.splice(idx-1, 3, eval(temp.slice(idx-1, idx+2).join('')));
            }
        }
        answer.push(Math.abs(temp[0]))
    }

    return Math.max(...answer);
}

console.log(solution("100-200*300-500+20"))
console.log(solution("50*6-3*2"))