// 내 풀이
function solution(phone_number) {
    let temp = phone_number.slice(0, -4);
    
    return phone_number.replace(temp, '*'.repeat(temp.length));
}

// 다른 사람 풀이
function solution2(s){
    return s.replace(/\d(?=\d{4})/g, "*");
}

const solution3 = n => [...n].fill("*",0,n.length-4).join("");

solution("01033334444");
solution2("027778888");