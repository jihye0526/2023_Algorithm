// 내 코드
function solution(sizes) {
    var arr1 = [];
    var arr2 = [];
    var x,y = 0;
    
    for(var i=0; i<sizes.length; i++){
        sizes[i].sort((a,b) => a-b);
        arr1.push(sizes[i][0]);
        arr2.push(sizes[i][1]);
    }
    
    x = Math.max(...arr1);
    
    for(var i=0; i<arr2.length; i++){
        if(arr2[i] < x){
            arr2[i] = 0
        }
    }
    
    y = Math.max(...arr2);
    
    return x*y;
}

// 다른 사람 코드
function solution2(sizes) {
    const rotated = sizes.map(([w, h]) => w < h ? [h, w] : [w, h]);

    let maxSize = [0, 0];
    rotated.forEach(([w, h]) => {
        if (w > maxSize[0]) maxSize[0] = w;
        if (h > maxSize[1]) maxSize[1] = h;
    })
    return maxSize[0]*maxSize[1];
}

console.log(solution([[60, 50], [30, 70], [60, 30], [80, 40]]));
console.log(solution2([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]));
console.log(solution2([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]));