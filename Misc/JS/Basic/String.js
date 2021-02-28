let st="abc"  

// concat
let a='ac'
let b='bd'

let c=a+' '+b
console.log(c);

// get a char
console.log(a[1]);


// length of string 
console.log(c.length);

// string methods
let temp='sdhhhhhhhhhhhhhhhhsA'
let email='abc@def.com'

// change case 
console.log(temp.toLowerCase(),temp);
console.log(temp.toUpperCase(),temp);

// get index
console.log(email.indexOf('@'),email.indexOf('c') );   //return 1st occ

// lastindex
console.log(email.lastIndexOf('c'));

// slice(from,to)
console.log(email.slice(0,4),email.slice(-3,-1));  //email[0:4],email[-3:-1] py
console.log(email.slice(0,15)); //doesnt throw error prints email  (CRAZY)

// substr(start,len)
console.log(email.substr(2,4));
console.log(email.substr(2,15)); //doesnt throw error prints only till end  (CRAZY)

// replace(org_char,replacement)
console.log(email.replace('a','r'));
console.log(email.replace('c','r'));  // replaces 1st occ only  abr@def.com


//includes  -return true if str includes given ar
console.log(email.includes('@')); //true
console.log(email.includes('!')); //false