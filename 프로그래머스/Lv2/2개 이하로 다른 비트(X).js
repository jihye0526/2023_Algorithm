// 다른 사람 풀이
function solution(nums) {
    var answer = [];
    
    for(let num of nums){
        if(num % 2 === 0){
            answer.push(num+1);
        }else{
            let numBin = "0" + num.toString(2);
            let len = numBin.length;
            
            for(let i=len-1; i>=0; i--){
                if(+numBin[i] === 0){
                    answer.push(parseInt(numBin.slice(0, i) + "10" + numBin.slice(i+2, len), 2));
                    break;
                }
            }
        }
    }
    
    return answer;
}

console.log(solution([2,7]));