const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = +input[0];
const arr = input[1].split(' ').map(Number);

const inc = Array.from({length:n}, () => 1);
const dec = Array.from({length:n}, () => 1);

for(let i=0; i<n; i++){
    for(let j=0; j<i; j++){
        if(arr[i] > arr[j]){
            inc[i] = Math.max(inc[i], inc[j]+1);
        }
    }
}

for(let i=n-1; i>=0; i--){
    for(let j=i+1; j<n; j++){
        if(arr[i] > arr[j]){
            dec[i] = Math.max(dec[i], dec[j]+1);
        }
    }
}

console.log(
    Math.max(...inc.map((el, i) => el+dec[i]-1))
);