// 내 풀이
function solution(record) {
    const answer = [];
    const nickname = {};
    const msg = {"Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."};
    
    record.map((el) => {
        const [sort, id, name] = el.split(" ");
        if(sort === "Enter" || sort === "Change") nickname[id] = name;
    });
    
    record.map((el) => {
        const [sort, id] = el.split(" ");
        if(sort === "Enter" || sort === "Leave") answer.push(nickname[id] + msg[sort]);
    });
    
    return answer;
}

// 다른 사람 풀이
function solution2(record) {
    const userInfo = {};
    const action = [];
    const stateMapping = {
        'Enter': '님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.'
    }

    record.forEach((v) => {
        const [state, id, nick] = v.split(' ');

        if(state !== "Change") {
            action.push([state, id]);
        }

        if(nick) {
            userInfo[id] = nick;
        }
    })

    return action.map(([state, uid]) => {
        return `${userInfo[uid]}${stateMapping[state]}`;    
    })
}

console.log(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
console.log(solution2(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))