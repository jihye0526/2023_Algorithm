// 내 풀이
function solution(nums) {
    let answer = 0;
    
    for(let i=0; i<nums.length-2; i++){
        for(let j=i+1; j<nums.length-1; j++){
            for(let k=j+1; k<nums.length; k++){
                if(decimal(nums[i]+nums[j]+nums[k]) === 0){
                    answer++;
                }
            }
        }
    }
    
    return answer;
}

function decimal(num){
    let cnt = 0;
    
    for(let i=2; i<=num**0.5; i++){
        num%i === 0 ? cnt++ : 0
    }
    
    return cnt;
}

console.log(solution([1,2,3,4]));
console.log(solution([1,2,7,6,4]));