// 내 풀이(시간초과)
function solution(ingredient) {
    let answer = 0;
    let recipe = "";
    
    for(var i of ingredient){
        recipe += i;
    }

    while(recipe.indexOf("1231") > -1){
        answer += 1;
        recipe = recipe.replace("1231", "");
    }
    return answer;
}

// 다른 사람 풀이
function solution2(ingredient){
    let answer = 0;
    const arr = [];

    for(let i of ingredient){
        arr.push(i);

        if (arr.slice(-4).join('') == '1231') {
            arr.splice(-4);
            answer++;
        }
    }

    return answer;
}

console.log(solution2([2, 1, 1, 2, 3, 1, 2, 3, 1]));
console.log(solution2([1, 3, 2, 1, 2, 1, 3, 1, 2]));