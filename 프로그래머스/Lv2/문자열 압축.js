// 내 풀이
function solution(s) {
    let answer = s.length;
    
    for(let i=1; i<=parseInt(s.length/2); i++){
        let str = "";
        let arr = [];
        
        for(let j=0; j<s.length; j+=i){
            arr.push(s.slice(j, j+i));
        }
        
        let cnt = 1;
        for(let j=0; j<arr.length; j++){
            if(j !== arr.length-1 && arr[j] === arr[j+1]){
                cnt++;
            }else{
                str += cnt !== 1 ? String(cnt) + arr[j] : arr[j];
                cnt = 1;
            }
        }
        
        if(answer > str.length) answer = str.length;
    }
    
    return answer;
}

console.log(solution("aabbaccc"))
console.log(solution("ababcdcdababcdcd"))
console.log(solution("abcabcdede"))
console.log(solution("abcabcabcabcdededededede"))
console.log(solution("xababcdcdababcdcd"))