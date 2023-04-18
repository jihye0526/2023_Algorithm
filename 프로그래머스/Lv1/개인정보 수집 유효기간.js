function solution(today, terms, privacies) {
    var answer = [];
    var [year, month, date] = today.split(".").map(Number);
    var todates = year * 12 * 28 + month * 28 + date;
    var t = {};
    terms.forEach((e) => {
      let [a, b] = e.split(" ");
      t[a] = Number(b);
    });
    privacies.forEach((e, i) => {
      var [day, term] = e.split(" ");
      day = day.split(".").map(Number);
      var dates = day[0] * 12 * 28 + day[1] * 28 + day[2] + t[term] * 28;
      if (dates <= todates) answer.push(i + 1);
    });
    return answer;
  }

console.log(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
console.log(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))