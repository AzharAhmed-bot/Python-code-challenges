


function hexWordSum(string){
  let words=string.split(" ")
  let total=0
  
  for(let word of words){
    let char=word.split("")
    for(let i=0;i<char.length;i++){
      if(char[i]==="S"){
        char[i]="5"
    }
     else if(char[i]==="O"){
        char[i]="0"
     }
    }
    char=char.join("")
    if(/^[0-9A-F]+$/.test(char)){
        total+=parseInt(char,16)
    }
  }
  return total
}

console.log(hexWordSum("ASSESS ANY BAD CODE AND TRY AGAIN"))
console.log(hexWordSum("DEFACE"))
console.log(hexWordSum("CODE"))
console.log(hexWordSum(""))