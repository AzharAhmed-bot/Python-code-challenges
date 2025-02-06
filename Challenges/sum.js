function summer(arr){
    var result=[]
    for(let i=0;i<arr.length-1;i++){
        let temp=arr[i]+arr[i+1]
        result.push(temp)
    }
    return result
}

function total(arr){
    while(arr.length>1){
        arr=summer(arr)
    }
    return arr[0]
}

console.log(total([1,2,3,4]))

