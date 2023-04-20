/**
 * 내 풀이
 * @param {number} k 
 * @param {Array} score 
 * @returns 
 */
function solution(k, score) {
    var answer = [];
    var result = [];
    
    for(var i=0; i<score.length; i++){
        if(answer.length < k){
            answer.push(score[i]);
        }else if(score[i] > Math.min(...answer)){
            var idx = answer.indexOf(Math.min(...answer));
            answer[idx] = score[i];
        }
        
        result.push(Math.min(...answer));
    }
    return result;
}

/**
 * 다른사람 풀이
 * @param {number} k 
 * @param {Array} score 
 * @returns 
 */
function solution2(k, score) {
    var answer = [];

    return score.reduce((a, c) => {
        answer.push(c);
        answer.sort((a, b) => a - b);

        if(answer.length > k){
            answer.shift();
        }

        a.push(answer[0]);
        return a;
    }, [])
}

console.log(solution(3, [10, 100, 20, 150, 1, 100, 200]));
console.log(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]));