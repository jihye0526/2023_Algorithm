// 다른 사람 풀이 1
function solution(n, wires) {
    var answer = n;
    
    for(let i=0; i<wires.length; i++){
        const parent = Array.from({length:n+1}, (_, i) => i);
        for(let j=0; j<wires.length; j++){
            if(i == j) continue;
            union_parent(parent, wires[j][0], wires[j][1]);
        }
        
        for(let wire of wires){
            let a = wire[0];
            let b = wire[1];
            
            parent[a] = find_parent(parent, a);
            parent[b] = find_parent(parent, b); 
        }
        
        s1 = parent.filter((el) => el === parent[wires[i][0]]).length;
        s2 = parent.filter((el) => el === parent[wires[i][1]]).length;
        answer = Math.min(answer, Math.abs(s1- s2));
    }
    
    return answer;
}

function union_parent(parent, a, b){
    a = find_parent(parent, a);
    b = find_parent(parent, b);
    
    if(a < b) parent[b] = a;
    else parent[a] = b;
}

function find_parent(parent, x){
    if(parent[x] !== x){
        return find_parent(parent, parent[x]);
    }
    
    return parent[x];
}

// 다른 사람 풀이 2
function solution2(n, wires) {
    let answer = n;
    const conn = Array.from({length: n+1}, () => []);
    
    for(let wire of wires){
        conn[wire[0]].push(wire[1]);
        conn[wire[1]].push(wire[0]);
    }
    
    for(let wire of wires){
        conn[wire[0]] = conn[wire[0]].filter(el => el !== wire[1]);
        conn[wire[1]] = conn[wire[1]].filter(el => el !== wire[0]);
            
        answer = Math.min(answer, Math.abs(bfs(wire[0], n, conn) - bfs(wire[1], n, conn)));
        
        conn[wire[0]].push(wire[1]);
        conn[wire[1]].push(wire[0]);
    }
    
    return answer;
}

function bfs(start, n, conn){
    let cnt = 0;
    const q = [start];
    const visited = Array.from({length:n+1}, () => false);
    
    while(q.length !== 0){
        let temp = q.pop();
        
        if(visited[temp] === false){
            q.push(...conn[temp]);
            visited[temp] = true;
            cnt++;
        }
    }
    
    return cnt;
}

console.log(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
console.log(solution(4, [[1,2],[2,3],[3,4]]))
console.log(solution2(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))