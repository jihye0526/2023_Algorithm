// 다른 사람 풀이
function solution(k, tangerine) {
    let answer = 0;
    let dict = {};
    
    for(let i=0; i<tangerine.length; i++){
        if(tangerine[i] in dict){
            dict[tangerine[i]] += 1;
        }else{
            dict[tangerine[i]] = 1;
        }
    }
    
    let arr = Object.values(dict);
    arr.sort((a, b) => b - a);
    
    for(let i=0; i<arr.length; i++){
        if(k > 0){
            k -= arr[i];
            answer += 1;
        }else{
            break;
        }
    }
    
    return answer;
}

function solution2(k, tangerine) {
    let answer = 0;
    const tDict = {};
    tangerine.forEach((t) => tDict[t] = (tDict[t] || 0) + 1);
    const tArr = Object.values(tDict).sort((a, b) => b - a);
    for (const t of tArr) {
      answer++;
      if (k > t) k -= t;
      else break;
    }
    return answer;
  }

console.log(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]));
console.log(solution2(4, [1, 3, 2, 5, 4, 5, 2, 3]));
console.log(solution2(2, [1, 1, 1, 1, 2, 2, 2, 3]));