// 내 풀이
function solution(d, budget) {
    let answer = 0;
    let cnt = 0;
    
    // d.sort()를 사용하면 d = [1, 10, 7, 5, 2]일 경우 [ 1, 10, 2, 5, 7 ]로 출력되므로 숫자를 기준으로 정렬하고 싶으면 아래와 같이 사용해야 함 
    d.sort((a, b) => a-b);
    
    for(let i of d){
        if(answer + i <= budget){
            answer += i;
            cnt += 1;
        }
        
    }
    
    return cnt;
}

console.log(solution([1,3,2,5,4], 9))
console.log(solution([2,2,3,3], 10))
console.log([1, 10, 7, 5, 2].sort())