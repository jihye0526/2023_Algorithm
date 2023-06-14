// 내 풀이
function solution(n, arr1, arr2) {
    let answer = [];

    let map1 = secret_map(n, arr1);
    let map2 = secret_map(n, arr2);

    for(let i=0; i<n; i++){
        let temp = [];
        for(let j=0; j<n; j++){
            if(map1[i][j] + map2[i][j] >= 1){
                temp.push('#');
            }else{
                temp.push(' ');
            }
        }
        answer.push(temp.join(''));
    }

    return answer;
}

function secret_map(n, arr){
    let answer = [];

    for(let i=0; i<n; i++){
        let num = arr[i];
        let temp = [];
        for(j=n-1; j>=0; j--){
            if(num >= 2**j){
                num -= 2**j;
                temp.push(1);
            }else{
                temp.push(0);
            }
        }
        answer.push(temp);
    }

    return answer;
}

// 다른 사람 풀이 1
function solution1(n, arr1, arr2) {
    return arr1.map((v, i) => addZero(n, (v | arr2[i]).toString(2)).replace(/1|0/g, a => +a ? '#' : ' '));
}

const addZero = (n, s) => {
    return '0'.repeat(n - s.length) + s;
}

// 다른 사람 풀이 2
var solution2=(n,a,b)=>a.map((a,i)=>(a|b[i]).toString(2).padStart(n,0).replace(/0/g,' ').replace(/1/g,'#'))

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution1(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution2(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));