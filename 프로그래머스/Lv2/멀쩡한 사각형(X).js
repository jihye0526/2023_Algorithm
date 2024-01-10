// 다른 사람 풀이
function solution(w, h) {
    return w * h - (w + h - gcd(w, h));
}

function gcd(a, b) {
    const mod = a % b;
    if (mod === 0) return b;
    return gcd(b, a % b);
}

console.log(solution(8, 12));