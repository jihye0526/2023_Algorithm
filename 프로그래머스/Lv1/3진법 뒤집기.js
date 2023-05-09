// 내 풀이
function solution(n) {
    let answer = "";
    let i = 1;
    let result = 0;

    while(3**i <= n){
        i++;
    }

    for(let j=i-1; j>-1; j--){
        for(let k=2; k>-1; k--){
            if((3**j)*k <= n){
                answer += String(k);
                n -= (3**j)*k;
                break;
            }
        }
    }

    for(let z=0; z<answer.length; z++){
        result += 3**z*answer[z];

    }
    return result;
}

// 다른 사람 풀이
const solution2 = (n) => {
    // {{10진수}}.toString(n) 를 사용해 10진수를 원하는 n진수로 변환
    // parseInt({{n진수}}, n) 를 사용해 n진수를 10진수로 변환
    return parseInt([...n.toString(3)].reverse().join(""), 3);
}

console.log(solution(45));
console.log(solution2(125));