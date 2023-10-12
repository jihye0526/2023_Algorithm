// 내 풀이
function solution(skill, skill_trees) {
    let answer = 0;
    
    for(let skill_tree of skill_trees){
        const temp = skill_tree.split('');
        let idx = 0;
        
        while(temp.length){
            if(!skill.includes(temp[0])){
                temp.shift();
            }else{
                if(idx == skill.indexOf(temp[0])){
                    temp.shift();
                    idx++;
                }else{
                    break;
                }
            }
        }
        
        if(temp.length == 0) answer++
    }
    
    return answer;
}

// 다른 사람 풀이
function solution2(skill, skill_trees) {
    var regex = new RegExp(`[^${skill}]`, 'g');

    return skill_trees
        .map((x) => x.replace(regex, ''))
        .filter((x) => {
            return skill.indexOf(x) === 0 || x === "";
        })
        .length
}

console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
console.log(solution2("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))