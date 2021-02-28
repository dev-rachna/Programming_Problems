// comparison

// eq
let age=25

console.log(age==25);
console.log(age=='25'); //true (CRAZY) doesnt care of type if == used
console.log(age!=30);
console.log(age!=25);

//  > <
console.log(age>20);
console.log(age<26);
console.log(age<='25'); //true 

// check for string behaviour --(CRAZY)

console.log('shaun'>'Shaun');  //true

// strict comparison
console.log(age==='25');  //false
console.log(age===25);  //true