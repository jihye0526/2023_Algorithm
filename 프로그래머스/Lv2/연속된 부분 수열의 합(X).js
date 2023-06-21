function solution(sequence, k) {
    let answer = [];
    let sum = 0;
    let start = 0;
    let end = 0;
    let len = sequence.length;
    
    for(let i=0; i<sequence.length; i++){
        end = i;
        sum += sequence[end];
        
        while(sum > k){
            sum -= sequence[start];
            start += 1;
        }
        
        if(sum === k && (end - start) < len){
            answer = [start, end];
            len = end - start;
        }
    }
    
    return answer;
}

console.log(solution([1,2,3,4,5], 7));
console.log(solution([1,1,1,2,3,4,5], 5));
console.log(solution([2,2,2,2,2], 6));