// 다른 사람 풀이 1
function solution(topping) {
    let answer = 0;
    let baseSet = new Set();
    let compareSet = new Set();
    let counter = new Array(10001).fill(0);
    
    topping.map(e => {
        baseSet.add(e);
        counter[e]++;
    });
    
    topping.map(e => {
        counter[e]--;
        
        if(counter[e] === 0) baseSet.delete(e);
        
        compareSet.add(e);
        
        if(baseSet.size === compareSet.size) answer++;
    });
    
    return answer;
}

console.log(solution([1, 2, 1, 3, 1, 4, 1, 2]));
console.log(solution([1, 2, 3, 1, 4]));