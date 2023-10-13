// 다른 사람 풀이
function solution(p) {
    let answer = '';
    let open = 0;
    let close = 0;
    
    if(!p) return '';
    
    for(let i=0; i<p.length; i++){
        if(p[i] === '(') open++;
        else close++;
        
        if(open === close){
            if(isCorrect(p.slice(0, i+1))){
                answer = p.slice(0, i+1) + solution(p.slice(i+1));
                return answer;
            }else{
                answer = "(" + solution(p.slice(i+1)) + ")";
                
                for(let j=1; j<i; j++){
                    if(p[j] === "("){
                        answer += ")";
                    }else{
                        answer += "(";
                    }
                }
                
                return answer;
            }
        }
    }
        
    
    return answer;
}

function isCorrect(arr){
    let result = [];
    
    for(let i of arr){
        if(i === "("){
            result.push(i);
        }else{
            if(result.length == 0) return false;
            result.pop();
        }
    }
    
    return true;
}

console.log(solution("(()())()"))
console.log(solution(")("))
console.log(solution("()))((()"))