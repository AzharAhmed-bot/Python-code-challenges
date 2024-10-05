function breakintoParts(string){
    const length=string.length
    const partsLenght=Math.floor(length/3);
    const remainder = length % 3;
    const parts=[]
    for(let i=0;i<3;i++){
        const start=i*partsLenght + (i< remainder ? i: remainder);
        const end= (i + 1) * partsLenght + (i < remainder ? i + 1 : remainder);
        parts.push(string.substring(start,end))
    }
    return parts.join(" ");
}


function encrypt(passcode) {
    const length=passcode.length
    let isAlpha='^[a-z]+$'
    // Test your secret agent skills here!
    if(length>9 && passcode.match(isAlpha)){
        return breakintoParts(passcode);
    }
    return "BANG!"
}

console.log(encrypt("hkndkndkknknello"))