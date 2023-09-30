// 내 풀이
function solution(n, t, m, p) {
    let answer = '';
    let num = 0;
    let str = '';
    
    while(true){
        let temp = num.toString(n);
        str += temp;
        num += 1
        
        if(str.length >= t*m) break;
    }
    
    for(let i=p-1; i<str.length; i+=m){
        answer += str[i];
        
        if(answer.length == t) break;
    }
    
    return answer.toUpperCase();
}

// 다른 사람 풀이
function solution2(n, t, m, p) {
    var tubeT = Array.apply(null,Array(t)).map((a,i)=>i*m+p-1);
    var line = '';
    var max = m*t + p;
    
    for (var i =0;line.length <= max; i++) {
        line += i.toString(n);
    }

    return tubeT.map(a=>line[a]).join('').toUpperCase();
}

console.log(solution(2, 4, 2, 1))
console.log(solution(16, 16, 2, 1))
console.log(solution(16, 16, 2, 2))