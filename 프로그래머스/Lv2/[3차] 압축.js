// 내 풀이
function solution(msg) {
    const answer = [];
    const dict = {};
    
    for(let i=1; i<27; i++){
        dict[String.fromCharCode(i+64)] = i;
    }
    
    while(msg.length){
        let tempIdx = -1;
        let temp = -1;
        
        for(let i=0; i<msg.length; i++){
            let str = msg.slice(0, i+1);
            
            if(str in dict){
                tempIdx = i+1;
                temp = dict[str];
            }else{
                let maxNum = Math.max(...Object.values(dict));
                dict[str] = parseInt(maxNum)+1;
                answer.push(temp);
                msg = msg.slice(tempIdx);
                break;
            }
            
            if(str === msg){
                answer.push(temp);
                msg = msg.slice(tempIdx);
            }
        }
    }
    
    return answer;
}

// 다른 사람 풀이
function solution2(msg) {
    var list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    var dic = list.reduce((d, a, i) => (d[a] = i + 1, d), {})

    var result = [];

    var maxLen = 1;
    for (var i = 0; i < msg.length; i++) {

        var w = msg[i];
        var c = msg[i+1];
        while (dic[w+c] && i < msg.length - 1) {
            i++;

            w = w+c;
            c = msg[i+1];
        }

        result.push(dic[w]);

        list.push(dic[w+c]);
        dic[w+c] = list.length;
    }

    return result;
}

console.log(solution("KAKAO"))
console.log(solution("TOBEORNOTTOBEORTOBEORNOT"))
console.log(solution2("ABABABABABABABAB"))