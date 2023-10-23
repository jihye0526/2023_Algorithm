// 다른 사람 풀이
function solution(name) {
    let answer = 0;
    let min_move = name.length - 1;
  
    [...name].map((n, i) => {
      answer += Math.min(n.charCodeAt() - 65, 91 - n.charCodeAt());
      let idx = i + 1;
  
      // 연속되는 A의 개수 count
      while (idx < name.length && name[idx] === 'A') {
        idx++;
      }
  
      min_move = Math.min(
        min_move,
        i * 2 + name.length - idx, // A 가 나오기 전까지 왼쪽에서 오른쪽으로 이동 => A 를 마주치면 처음으로 돌아감 => 문자열의 끝에서 왼쪽으로 이동하면서 A 를 만나기 전까지 이동
        i + 2 * (name.length - idx), // 뒤에서부터 idx까지 왔다가, 다시 돌아가서 앞에서부터 현재 인덱스 전까지 오는 경우
      );
    });
  
    return answer + min_move;
  }
  
  console.log(solution("BBBAABB"))
  console.log(solution("JEROEN"))
  console.log(solution("JAN"))
  console.log(solution("JAZ"))
  console.log(solution("AAAABBCCC"))