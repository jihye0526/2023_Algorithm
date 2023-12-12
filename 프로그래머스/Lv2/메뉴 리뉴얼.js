// 내 풀이
function solution(orders, course) {
    const answer = [];
    const combinations = [];
    const arr = [];
    
    // 모든 경우의 수 구하기
    for(let order of orders){
        order = order.split("");
        for(let i=2; i<=order.length; i++){
            combinations.push(...combi(order, i));
        }
    }
    
    // 중복 제거
    const set = new Set(combinations);
    
    for(let s of set){
        // set의 원소가 combinations에 몇 개 들어있는지 filter
        const cnt = combinations.filter(el => el === s).length;
        
        // 메뉴가 2번 이상 조합되어야함
        if(cnt > 1) arr.push([s, cnt]);
    }
    
    arr.sort((a, b) => a[0].length - b[0].length || b[1] - a[1]);
    
    for(let i of course){
        let maxArr = arr.filter(el => el[0].length === i);
        
        if(maxArr.length !== 0){
            // 메뉴 구성 길이중에 max값
            const maxCnt = maxArr[0][1];
            maxArr = maxArr.filter(el => el[1] === maxCnt);
            
            answer.push(...maxArr.map(el => el[0]));
        }
    }
    
    return answer.sort();
}

function combi(arr, idx){
    const result = [];
    if(idx === 1) return arr.map(el => [el]);
    
    arr.map((curr, i, origin) => {
        const rest = origin.slice(i+1);
        const temp = combi(rest, idx-1);
        const attached = temp.map(el => [curr, ...el]);
        result.push(...attached.map(el => el.sort().join("")));
    });
    
    return result;
}

// 다른 사람 풀이
function solution2(orders, course) {
    const ordered = {};
    const candidates = {};
    const maxNum = Array(10 + 1).fill(0);
    const createSet = (arr, start, len, foods) => {
      if (len === 0) {
        ordered[foods] = (ordered[foods] || 0) + 1;
        if (ordered[foods] > 1) candidates[foods] = ordered[foods];
        maxNum[foods.length] = Math.max(maxNum[foods.length], ordered[foods]);
        return;
      }
  
      for (let i = start; i < arr.length; i++) {
        createSet(arr, i + 1, len - 1, foods + arr[i]);
      }
    };
  
    orders.forEach((od) => {
      // arr.sort는 기본적으로 사전식 배열
      const sorted = od.split('').sort();
      // 주문한 음식을 사전순으로 배열해서 문자열을 만든다.
      // course에 있는 길이만 만들면 된다.
      course.forEach((len) => {
        createSet(sorted, 0, len, '');
      });
    });
  
    const launched = Object.keys(candidates).filter(
      (food) => maxNum[food.length] === candidates[food]
    );
  
    return launched.sort();
  }

console.log(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
console.log(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
console.log(solution2(["XYZ", "XWY", "WXA"], [2,3,4]))