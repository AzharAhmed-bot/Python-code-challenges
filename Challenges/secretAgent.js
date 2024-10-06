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
};
function reverseBreakintoParts(string){
    const length=string.length
    const partsLenght=Math.floor(length/3);
    const remainder = length % 3;
    const parts=[]
    for(let i=0;i<3;i++){
        const start=i*partsLenght + (i< remainder ? i: remainder);
        const end= (i + 1) * partsLenght + (i < remainder ? i + 1 : remainder);
        parts.push(string.substring(start,end))
    }

    // Check if the middle part has any numbers in it
    const middlePart = parts[1];
    const lastPart = parts[2];
    const numbersInMiddlePart = middlePart.replace(/[^0-9]/g, '');
    if (numbersInMiddlePart.length > 0) {
        parts[1] = middlePart.replace(/[0-9]/g, '');
        parts[2] = lastPart + numbersInMiddlePart;
    }

    return parts;
};


function isOdd(number){
    return number%2!==0
}
function alphabetToNumber(string){
    const parts=breakintoParts(string).split(" ");
    const partOne=parts[0]
    const result=[]
    for(let i=0;i<partOne.length;i++){
        if(!isOdd(i)){
        result.push(partOne[i].charCodeAt(0)-96)
    }
        else{
            result.push(partOne[i]);
        }
    }
    return result.join("");
}
function undoAlphabetToNumbers(partThree){
    let result=''
    for(let i=0;i<partThree.length;i++){
        if(!isNaN(partThree[i])){
            result+=String.fromCharCode(partThree[i]+96)
        }else{
            result+=partThree[i]
        }
    }
    return result;
}

function reverse(string){
    const partTwo=breakintoParts(string).split(" ")[1];
    return partTwo.split("").reverse().join("")
}
function undoReverse(partTwo){
    return partTwo.split("").reverse().join("");
}


function substitute(string){
    const partThree=breakintoParts(string).split(" ")[2];
    let result='';
    for(let i=0;i<partThree.length;i++){
        const charCode=partThree.charCodeAt(i);
        if(charCode===122){
            result+='a'
        }else{
            result+=String.fromCharCode(charCode+1)
        }
    }
    return result
}
function undoSubstitute(partThree){
    let result='';
    for(let i=0;i<partThree.length;i++){
        const charCode=partThree.charCodeAt(i);
        if(charCode===97){
            result+='z'
        }else{
            result+=String.fromCharCode(charCode-1)
        }
    }
}


function encrypt(passcode) {
    const length=passcode.length
    let isAlpha='^[a-z]+$'
    // Test your secret agent skills here!
    if(length>=9 && passcode.match(isAlpha)){
        const partOne=alphabetToNumber(passcode);
        const partTwo=reverse(passcode);
        const partThree=substitute(passcode);
        return partTwo+""+partThree+""+partOne
    }
    return "BANG!"
};

// var validPasscodes = passcodes;

function decrypt(password) {
    const [partTwo, partThree, partOne] = reverseBreakintoParts(password);
    const originalPartThree = undoSubstitute(partThree);
    const originalPartTwo = undoReverse(partTwo);
    const originalPartOne = undoAlphabetToNumbers(partOne);

    const decryptedPasscode = originalPartOne + originalPartTwo + originalPartThree;
    if (isValidString(decryptedPasscode)) {
        return "Nice to meet you, fellow Agent!";
    }
    return "BANG!";
}
function isValidString(passcode) {
    return /^[a-z]+$/.test(passcode) && passcode.length >= 9;
}

console.log(encrypt("paparazzi"));
console.log(reverseBreakintoParts("bsepoe10a13"))
console.log(decrypt("araaaj16a16"));