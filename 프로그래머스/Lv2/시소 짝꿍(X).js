// 다른 사람 풀이
function solution(weights) {
    let answer = 0;
    const ratio = [1, 3/2, 4/3, 2];
    const dict = {};
    
    weights.sort((a, b) => b - a).forEach((w) => {
       ratio.forEach(r => {
           if(dict[w*r]) answer += dict[w*r];
       });
        
        if(!dict[w]) dict[w] = 1;
        else dict[w] += 1;
    });
    
    return answer;
}

// 오름 차순 정렬을 원하면 아래와 같이 사용 가능
function solution2(weights) {
    let answer = 0;
    const ratio = [1, 2/3, 3/4, 1/2];
    const dict = {};
    
    weights.sort((a, b) => a - b).forEach((w) => {
       ratio.forEach(r => {
           if(dict[w*r]) answer += dict[w*r];
       });
        
        if(!dict[w]) dict[w] = 1;
        else dict[w] += 1;
    });
    
    return answer;
}

console.log(solution([100,180,360,100,270]));
console.log(solution2([100,180,360,100,270]));