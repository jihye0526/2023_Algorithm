// 내 풀이
function solution(food) {
    var answer = '';
    var dict = {};
    
    food.forEach((f, idx) => dict[idx] = parseInt(f/2));
    
    for(var i=1; i<food.length; i++){
        for(var cnt=1; cnt<dict[i]+1; cnt++){
            answer += i;
        }
    }
    
    answer += "0";

    for(var i=food.length; i>0; i--){
        for(var cnt=1; cnt<dict[i]+1; cnt++){
            answer += i;
        }
    }
    
    return answer;
}

// 다른 사람 풀이
function solution2(food) {
    let res = '';
    for (let i = 1; i < food.length; i++) {
        res += String(i).repeat(Math.floor(food[i]/2));
    }

    return res + '0' + [...res].reverse().join('');
}

console.log(solution([1, 3, 4, 6]))
console.log(solution2([1, 7, 1, 2]))