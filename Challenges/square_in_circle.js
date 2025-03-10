function biggestSquareInCircle(radius) {
    // s sqrt(2)= 2r
    let side= 2*radius / Math.sqrt(2);
    return Math.round(side*side);
}

console.log(biggestSquareInCircle(5))