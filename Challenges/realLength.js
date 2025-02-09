const { get } = require("http")

function getRealLength(string){
    let count=0
    for(let i=0;i<string.length;i++){
       const code=string.charCodeAt(i)
       if(code>=0xD800 && code<=0xDBFF){
        i++
       }
       count++
    }
    return count
}
const getLength=(string)=>[...string].length
console.log(getLength('😸🦌🚀'))
console.log(getRealLength("😸🦌🚀"))