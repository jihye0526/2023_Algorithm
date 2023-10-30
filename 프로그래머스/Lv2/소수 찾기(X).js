function solution(numbers) {
    let answer = 0;
    const numArr = numbers.split("");
    let cases = [];
    
    for(let i=numbers.length; i>0; i--){
        const temp = getPerm(numArr, i);
        cases.push(...temp.map(el => parseInt(el.join(""))));
    }
    cases = new Set(cases);
    
    for(let c of cases){
        if(c === 0 || c === 1) continue;
        
        let cnt = 0;
        for(let i=2; i<=c**0.5; i++){
            if(c%i === 0) cnt++;
        }
        if(cnt === 0) answer++;
    }
    
    return answer;
}

function getPerm(arr, n){
    const result = [];
    
    if(n === 1) return arr.map(el => [el]);
    
    arr.forEach((fixed, i, origin) => {
        const rest = [...arr.slice(0, i), ...arr.slice(i+1)];
        const perm = getPerm(rest, n-1);
        const attch = perm.map(el => [fixed, ...el]);
        result.push(...attch);
    });
    
    return result
}

console.log(solution("17"))
console.log(solution("011"))