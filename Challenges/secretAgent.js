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
function reverseBreakintoParts(string) {
    let lastPartStart =string && string.search(/\d+[a-zA-Z]?\d*$/);
    const lastPart =string && string.slice(lastPartStart);
    const firstTwoParts = string.slice(0, lastPartStart);
    const mid = Math.floor(firstTwoParts && firstTwoParts.length / 2);

    const part1 =firstTwoParts && firstTwoParts.slice(0, mid);
    const part2 =firstTwoParts && firstTwoParts.slice(mid);

    return [part1, part2, lastPart];
}



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
function undoAlphabetToNumbers(partOne) {
    let result = '';
    let i = 0;

    while (i < partOne.length) {
        if (!isNaN(partOne[i])) { 
            let num = '';
            while (i < partOne.length && !isNaN(partOne[i])) {
                num += partOne[i];
                i++;
            }
            result += String.fromCharCode(parseInt(num) + 96);
        } else { 
            result += partOne[i];
            i++;
        }
    }
    
    return result;
}

// Working
function reverse(string){
    const partTwo=breakintoParts(string).split(" ")[1];
    return partTwo.split("").reverse().join("")
}

// Working
function undoReverse(partTwo){
    return partTwo.split("").reverse().join("");
}

// Working
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

// Working
function undoSubstitute(partThree){
    let result='';
    for(let i=0;i<partThree && partThree.length;i++){
        const charCode=partThree.charCodeAt(i);
        if(charCode===97){
            result+='z'
        }else{
            result+=String.fromCharCode(charCode-1)
        }
    }
    return result
}


function encrypt(passcode) {
    const length=passcode.length
    let isAlpha='^[a-z]+$'
    // Test your secret agent skills here!
    if(length>=9 && passcode.match(isAlpha)){
        const partOne=alphabetToNumber(passcode);
        const partTwo=reverse(passcode);
        const partThree=substitute(passcode);
        const encryptedString = partTwo+""+partThree+""+partOne;
        const numbers = encryptedString.match(/\d+/g);
        let totalLength = encryptedString.length;
        for (let i = 0; i < numbers.length; i++) {
            totalLength -= numbers[i].length - 1;
        }
        if (totalLength === 9) {
            return encryptedString;
        } else {
            return "BANG!";
        }
    }
    return "BANG!";
};

var validPasscodes = ["jamesbond","paparazzi","blackjack"];

function decrypt(password) {
    const [partTwo, partThree, partOne] = reverseBreakintoParts(password);
    const originalPartThree = undoSubstitute(partThree);
    const originalPartTwo = undoReverse(partTwo);
    const originalPartOne = undoAlphabetToNumbers(partOne);

    console.log(originalPartOne,originalPartTwo,originalPartThree)
    const decryptedPasscode = originalPartOne + originalPartTwo + originalPartThree;
    if (isValidString(decryptedPasscode)) {
        if(validPasscodes.includes(decryptedPasscode)){
            return "Nice to meet you, fellow Agent!";
        }
        return "BANG!"
    }
    return "BANG!";
}
function isValidString(passcode) {
    return /^[a-z]+$/.test(passcode) && passcode.length >= 9;
}

console.log(encrypt("jamesbond"));
console.log(decrypt("araaaj16a16"));