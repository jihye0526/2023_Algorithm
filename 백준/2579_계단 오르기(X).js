// 다른 사람 풀이
const fs = require('fs');
const [n, ...input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n").map(Number);
const dp = new Array(n).fill(0);

dp[0] = input[0];
dp[1] = input[0] + input[1];
dp[2] = Math.max(input[0], input[1]) + input[2];

for(let i=3; i<n; i++){
    dp[i] = Math.max(dp[i-2]+input[i], dp[i-3]+input[i-1]+input[i]);
}

console.log(dp[n-1]);