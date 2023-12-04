// 내 풀이
function solution(bandage, health, attacks) {
    const [last, recovery, bonus] = bandage;
    const lastAttack = attacks[attacks.length-1][0];
    let accumulate = 0;
    const maximum = health;
    
    for(let i=1; i<=lastAttack; i++){
        const [attackTime, damage] = attacks[0];
        
        if(i === attackTime){
            attacks.shift();
            health -= damage;
            accumulate = 0;
            if(health <= 0) return -1;
        }else{
            if(accumulate < last){
                health += recovery;
                accumulate++;
            }
            
            if(accumulate === last){
                health += bonus;
                accumulate = 0;
            }
            
            if(health > maximum) health = maximum;
        }
    }
    
    return health;
}

function solution2(bandage, health, attacks) {
    let currHealth = health;
    let currTime = 0;
  
    for (let [attackTime, damage] of attacks) {
      let diffTime = attackTime - currTime - 1;
      currHealth += diffTime * bandage[1] + Math.floor(diffTime / bandage[0]) * bandage[2];
  
      if (currHealth > health) currHealth = health;
      currHealth -= damage;
      if (currHealth <= 0) return -1;
      currTime = attackTime;
    }
  
    return currHealth;
  }
  
console.log(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
console.log(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
console.log(solution2([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
console.log(solution2([1, 1, 1], 5, [[1, 2], [3, 2]]))