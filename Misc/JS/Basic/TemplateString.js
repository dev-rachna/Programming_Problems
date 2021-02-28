const title="RICH DAD POOR DAD"
const author='Robert Ki....'
const likes=10

// concat usual way
let result='the book'+title+'by'+author+'has'+likes+'likes'
console.log(result);

// template String
 result=`the book ${title} and ${author} and ${likes}`
console.log(result);