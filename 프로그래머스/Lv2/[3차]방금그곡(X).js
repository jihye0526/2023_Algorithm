// 내 풀이 (테스트케이스 27번 통과 X)
function solution(m, musicinfos) {
    const answer = [];
    m = m.replace(/(C#)/g,'c')
         .replace(/(D#)/g,'d')
         .replace(/(F#)/g,'f')
         .replace(/(G#)/g,'g')
         .replace(/(A#)/g,'a')
         .replace(/(E#)/g,'e'); 
    
    for(let musicinfo of musicinfos){
        let [start, end, title, music] = musicinfo.split(",");
        music = music.replace(/(C#)/g,'c')
                     .replace(/(D#)/g,'d')
                     .replace(/(F#)/g,'f')
                     .replace(/(G#)/g,'g')
                     .replace(/(A#)/g,'a')
                     .replace(/(E#)/g,'e'); 
        const [sH, sM] = start.split(":").map(Number);
        const [eH, eM] = end.split(":").map(Number);
        let playing = (eH * 60 + eM) - (sH * 60 + sM);
        let temp ="";
        
        for(let i=0; i<playing; i++){
            temp += music[i%music.length];
        }
        
        while(temp.indexOf(m) > -1){
            answer.push([title, playing]);
            temp = temp.substr(0, m-1) + temp.substr(temp.indexOf(m) + m.length);
        }
    }
    
    answer.sort((a, b) => b[1] - a[1] || b[0].length - a[0].length);
    
    return answer.length === 0 ? "(None)" : answer[0][0];
}

// 다른 사람 풀이 1
function solution2(m, musicinfos) {
    var answer = [];
    
    // 1.주어진 노래들을 객체로 만들어서 배열에 입력받는다.
    let song = [];
    for(let i=0; i<musicinfos.length; i++){
        let start, end, title, code;
        let temp = musicinfos[i].split(',');
        start = temp[0];
        end = temp[1];
        title = temp[2];
        code = temp[3].replace(/(C#)/g,'c')
                      .replace(/(D#)/g,'d')
                      .replace(/(F#)/g,'f')
                      .replace(/(G#)/g,'g')
                      .replace(/(A#)/g,'a');        
        song.push({'start':start, 'end':end, 'title':title, 'code':code});
    }
    
    // 2.노래들의 playTime을 구한다.
    for(let i=0; i<song.length; i++){
        let time = song[i].start.split(':');
        time = time.concat(song[i].end.split(':'))        
        
        let playTime = 60*(time[2] - time[0]) + (time[3] - time[1]);
        song[i].playTime = playTime;
        if(playTime < song[i].code.length){            
            song[i].code = song[i].code.slice(0, playTime);
        }                
        else{
            song[i].code = song[i].code.repeat(playTime / song[i].code.length + 1);
        }
    }        
    // 3. 노래 목록에 주어진 노래가 있는지 찾아본다.
    m = m.replace(/(C#)/g,'c')
         .replace(/(D#)/g,'d')
         .replace(/(F#)/g,'f')
         .replace(/(G#)/g,'g')
         .replace(/(A#)/g,'a');      
    for(let i=0; i<song.length; i++){
        if(song[i].code.includes(m))
            answer.push(song[i])
    }
    // 4. 노래 들을 조건에 맞게 정렬한다.
    answer.sort((a,b) => {
        let A = a.playTime;
        let B = b.playTime;
        if(A>B) return -1;
        else if(A<B) return 1;
        else return 0;
    });
    
    if(answer.length === 0)
        return '(None)';
    return answer[0].title;
}

// 다른 사람 풀이 2
const solution3 = (m, musicInfos) => {
    let answer = '';

    musicInfos = musicInfos.map(e => {
        let eArr = e.split(',');
        let timeDiff = (new Date(`1970-01-01 ${eArr[1]}:00`) - new Date(`1970-01-01 ${eArr[0]}:00`)) / 60000;
        let melody = eArr[3].replace(/[A-Z]#/g,m => m[0].toLowerCase());
        melody = melody.repeat(Math.ceil(timeDiff / melody.length)).substr(0, timeDiff);
        return `${timeDiff},${eArr[2]},${melody}`;
    });

    musicInfos.sort((a,b) => b.split(',')[0] - a.split(',')[0]);

    answer = musicInfos.filter(e => e.split(',')[2].indexOf(m.replace(/[A-Z]#/g,m => m[0].toLowerCase())) != -1);

    return answer.length == 0 ? '(None)' : answer[0].split(',')[1];
}

console.log(solution( "ABCDEFG", ["11:50,12:04,HELLO,CDEFGAB", "12:57,13:11,BYE,CDEFGAB"]))
console.log(solution2("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
console.log(solution2("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
console.log(solution3("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))