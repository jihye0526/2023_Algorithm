// 내 풀이
function solution(arr)
{
    let answer = [arr[0]];
    
    for(let i=1; i<arr.length; i++){
        arr[i-1] !== arr[i] ? answer.push(arr[i]) : 0;
    }
    
    return answer;
}

// 다른 사람 풀이
function solution2(arr)
{
    return arr.filter((val,index) => val != arr[index+1]);
}

console.log(solution([1,1,3,3,0,1,1]));
console.log(solution2([4,4,4,3,3]));