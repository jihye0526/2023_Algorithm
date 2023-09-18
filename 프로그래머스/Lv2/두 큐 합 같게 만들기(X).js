// 내 풀이 ( 시간 초과 )
function solution(q1, q2) {
    let answer = 0;
    let sum1 = q1.reduce((a,c) => a+c, 0);
    let sum2 = q2.reduce((a,c) => a+c, 0);
    
    while(q1.length && q2.length){
        if(sum1 > sum2){
            let temp = q1.shift();
            q2.push(temp);
            sum1 -= temp;
            sum2 += temp;
            answer++;
        }else if(sum1 < sum2){
            let temp = q2.shift();
            q1.push(temp);
            sum1 += temp;
            sum2 -= temp;
            answer++;
        }

        if(sum1 === sum2){
            return answer;
        }
    }
    
    return -1;
}

// 다른 사람 풀이
const solution2 = (queue1, queue2) => {
    let sum1 = queue1.reduce((prev, cur) => prev + cur, 0);
    let sum2 = queue2.reduce((prev, cur) => prev + cur, 0);
    const half = (sum1 + sum2) / 2;
    const q = [...queue1, ...queue2];
    let q1Pointer = 0;
    let q2Pointer = queue1.length;
  
    for (let cnt = 0; cnt < queue1.length * 3; cnt++) {
      if (sum1 === half) {
        return cnt;
      }
      sum1 =
        sum1 > half
          ? sum1 - q[q1Pointer++ % q.length]
          : sum1 + q[q2Pointer++ % q.length];
    }
  
    return -1;
  };