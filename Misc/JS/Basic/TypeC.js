let score='100'

console.log(score+1);//1001

score=Number(score)
console.log(score+1); //101

let str='Hello'

str=Number(str)
console.log(str);  //NaN  (CRAZY) doesnt throw error

let a=10
console.log(String(a));


// Boolean --converts based on truthy and falsy values (CRAZY)
console.log(Boolean(a)); //true
console.log(Boolean(0)); //false

