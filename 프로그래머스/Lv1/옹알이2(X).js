// 다른 사람 풀이1
function solution(babbling) {
    let answer = 0;
    const arr = ["aya", "ye", "woo", "ma"];
    
    for(let i=0; i<babbling.length; i++){
        let babble = babbling[i];
        
        for(let j=0; j<arr.length; j++){
            if(babble.includes(arr[j].repeat(2))){
                break;
            }
            
            babble = babble.split(arr[j]).join(" ");
        }
        
        if(babble.split(" ").join("").length === 0){
            answer += 1;
        }
    }
    return answer;
}

// 다른 사람 풀이2
function solution2(babbling) {
    const regexp1 = /(aya|ye|woo|ma)\1+/; // 두번 이상 같은 말이 반복되는 조건
    const regexp2 = /^(aya|ye|woo|ma)+$/; // 해당 단어들의 반복으로만 이루어졌다는 조건
  
    return babbling.reduce((ans, word) => (
      !regexp1.test(word) && regexp2.test(word) ? ++ans : ans
    ), 0);
}

console.log(solution(["aya", "yee", "u", "maa"]));
console.log(solution2(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]));