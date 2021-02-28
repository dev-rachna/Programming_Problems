const fs=require('fs')

// blocking io
const res=fs.readFileSync('temp.txt','utf-8')
console.log(res);
fs.writeFileSync('temp1.txt',res)


// non-blocking async 
fs.readFile('temp.txt','utf-8',function(err,data){
if (err){

}
else{
  console.log('data read ',data);
  fs.writeFile('temp1.txt',data,function (err) {
    if (err){}
    else{
      console.log('data written');
    }
  })
}
})
console.log('test');