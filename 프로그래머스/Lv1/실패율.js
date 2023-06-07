// 내 풀이
function solution(N, stages) {
    let answer = [];
    let level = {};
    let level_ratio = {};
    let total = stages.length;
    
    for(let i=1; i<N+1; i++){
        let cnt = stages.filter((x) => i === x);
        level[String(i)] = cnt.length;
    }
    
    for(let i in level){
        level_ratio[String(i)] = level[i] / total;
        total -= level[i];
    }
    
    level_ratio = Object.entries(level_ratio).sort((a, b) => b[1] - a[1]);
    
    for(let i=0; i<level_ratio.length; i++){
        answer.push(parseInt(level_ratio[i][0]));
    }
    
    return answer;
}

// 다른 사람 풀이
function solution2(N, stages){
    let answer = [];

    for(let i=1; i<=N; i++){
        let cnt = stages.filter((x) => x === i).length;
        let ratio = stages.filter((x) => x >= i).length;

        answer.push([i, cnt/ratio]);
    }

    answer.sort((a, b) => b[1] - a[1]);

    return answer.map((i) => i[0]);
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
console.log(solution2(4, [4,4,4,4,4]));