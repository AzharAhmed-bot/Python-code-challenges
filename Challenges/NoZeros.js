// I dont want trailing zeros
// Possible solution:
// 1. Check how many times the number is divisible by ten
// Convert my num to array

function noBoringZeros(n){
    let i=0
    let result=n
    if(n==0){
      return n
    }
    while((result%10==0)){
      const newResult=result/10
      result=newResult
      i++
    }
    return result
}

console.log(noBoringZeros(0))
console.log(noBoringZeros(1450))
console.log(noBoringZeros(960000))
console.log(noBoringZeros(1050))
console.log(noBoringZeros(-1050))