// 다른 사람 풀이 1
function solution(w, h) {
    return w * h - (w + h - gcd(w, h));
}

function gcd(a, b) {
    const mod = a % b;
    if (mod === 0) return b;
    return gcd(b, a % b);
}

// 다른 사람 풀이 2
function solution2(w,h){
    const slope = h / w;
    let result = 0;

    for(let i = 1; i <= w; i++){
        result += Math.ceil(slope * i);
    }

    return ((h * w) - result) * 2;
}

console.log(solution(8, 12));
console.log(solution2(8, 12));