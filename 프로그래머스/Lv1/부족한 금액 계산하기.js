// 내 풀이
function solution(price, money, count) {
    let answer = 0;
    let total = 0;
    
    for(var i=1; i<count+1; i++){
        total += price * i;
    }
    
    if(total > money){
        answer = total - money;
    }

    return answer;
}

// 다른 사람 풀이
function solution2(price, money, count) {
    const tmp = price * count * (count + 1) / 2 - money;
    return tmp > 0 ? tmp : 0;
}

console.log(solution(3,20,4));
console.log(solution2(3,20,4));