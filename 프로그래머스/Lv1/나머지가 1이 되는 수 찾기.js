function solution(n) {
    var answer = 0;
    var notFound = true;
    
    while(notFound){
        answer += 1;
        if(n % answer == 1){
            notFound = false;
        }
    }
    
    return answer;
}

console.log(solution(10));
console.log(solution(12));