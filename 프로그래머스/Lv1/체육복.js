function solution(n, lost, reserve) {
    let answer = 0;
    let arr = Array(n);
    arr.fill(1);
    
    lost.forEach((i) => arr[i-1]--);
    reserve.forEach((i) => arr[i-1]++);
    
    for(var i=0; i<n; i++){
        if(arr[i] === 2&& arr[i-1] === 0){
            arr[i]--;
            arr[i-1]++;
        }else if(arr[i] === 2 && arr[i+1] === 0){
            arr[i]--;
            arr[i+1]++;
        } 
    }
    
    
    for(let i of arr){
        i > 0 ? answer++ : 0;
    }
    
    return answer;
}

console.log(solution(5, [2, 4], [1, 3, 5]));
console.log(solution(5, [2, 4], [3]));
console.log(solution(3, [3], [1]));