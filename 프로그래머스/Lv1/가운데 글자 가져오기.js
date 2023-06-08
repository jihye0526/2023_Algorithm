// 내 풀이
function solution(s) {
    let i = s.length / 2;
    //str.substring(시작 인덱스번호, 끝 인덱스번호)
    return s.length % 2 ? s[Math.floor(i)] : s.substring(i-1, i+1); 
}

// 다른 사람 풀이
function solution2(s) {
    // str.substr(시작 인덱스, 추출 갯수)
    return s.substr(Math.ceil(s.length/2)-1, s.length%2 ? 1 : 2);
}

console.log(solution("abcde"));
console.log(solution2("qwer"));