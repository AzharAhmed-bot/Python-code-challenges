function sumOfSums(n){
    let sum=[]
    let result=BigInt(0)
    for(let i=1;i<=n;i++){
        const sumUpToI=BigInt(i*(i+1)/2);
        sum.push(sumUpToI);
    }

    const sumOfSum= sum.reduce((acc,num)=>acc+num,BigInt(0));
    for(let i=1;i<=sumOfSum;i++ ){
        result+=BigInt(i)
    }

    return result;
    
}

// Optimized code
function sumOfSumsOptimized(n){
    // Calculate the sum of the 1st n triangular numbers directly
    const triangularSum=BigInt(n*(n+1)*(n+2)/6);
    const result=triangularSum * (triangularSum+BigInt(1))/ BigInt(2);
    return result;
}

console.log(sumOfSums(3))
console.log(sumOfSumsOptimized(3))