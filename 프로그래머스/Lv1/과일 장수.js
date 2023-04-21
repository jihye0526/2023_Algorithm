function solution(k, m, score) {
    var answer = 0;

    score.sort((a, b) => b-a);
    var box = parseInt(score.length / m);

    for(var i=0; i<box; i++){
        answer += score[(i+1)*m-1] * m

    }
    return answer;
}

console.log(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]));
console.log(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]));