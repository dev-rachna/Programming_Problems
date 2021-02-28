let arr=['ab','bc','cd'] //declaration

console.log(arr);

// get particular ele
console.log(arr[2]);

console.log(arr[10]);  //undefined  (CRAZY) no error

// overwrite
arr[1]='rd'
console.log(arr);
// doesnt throw error
// arr[10]='fg'
// console.log(arr);  //[ 'ab', 'rd', 'cd', <7 empty items>, 'fg' ] (CRAZY!!!)


// methods

// join(string)--takes array and convers to string
console.log(arr.join(','));  //py eq-- ','.join(arr)

// indexOf
console.log(arr.indexOf('ab')); //if not present the returns -1

// concat  --same python extends
console.log(arr.concat([10,20]));

// push-returns len after adding ele to arr
console.log(arr.push(10),arr); //same as arr.append(ele)

// pop -pops out last value of arr
console.log(arr.pop(),arr);  //same arr.pop() in py

// includes
console.log(arr.includes('ab'));