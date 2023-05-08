// 내 풀이
function solution(a, b) {
    return a.reduce((a, c, i) => a + (c * b[i]), 0);
}

// 다른 사람 풀이
function solution2(a, b) {
    return a.reduce((acc, _, i) => acc += a[i] * b[i], 0); // 인자에 _ 를 넣는 것은 사용하지 않는 인자일 경우
}

console.log(solution([1,2,3,4], [-3,-1,0,2]));
console.log(solution2([-1,0,1], [1,0,-1]));