function ofThe(arr, str) {
    let result = [];
    if (arr.length === 0 || arr.length === 1) {
      return arr;
    } else if (str === "") {
      return arr;
    }
  
    // Sort with custom comparison function to maintain order for duplicates
    const sortedArray = arr.sort((a, b) => {
      if (a !== b) {
        return a - b; // Sort by value first
      }
      // If values are equal, sort by original index (ascending)
      return arr.indexOf(a) - arr.indexOf(b);
    });
  
    const halflength = Math.floor(sortedArray.length / 2);
    const firstHalf = sortedArray.slice(0, halflength);
    const secondHalf = sortedArray.slice(halflength);
  
    switch (str) {
      case "the biggest of the smallest":
        if (firstHalf.length % 2 === 0) {
          result = firstHalf.slice(firstHalf.length / 2);
        } else {
          result = firstHalf.slice(Math.floor(firstHalf.length / 2));
        }
        break;
      case "the smallest of the biggest":
        if (secondHalf.length % 2 === 0) {
          result = secondHalf.slice(secondHalf.length / 2);
        } else {
          result = secondHalf.slice(Math.floor(secondHalf.length / 2));
        }
        break;
      case "the smallest of the biggest of the biggest":
        if (secondHalf.length % 2 === 0) {
          const secondHalfMiddleIndex = Math.floor(secondHalf.length / 2);
          result = [secondHalf[secondHalfMiddleIndex - 1]];
        } else {
          const secondHalfMiddleIndex = Math.floor(secondHalf.length / 2);
          result = [secondHalf[secondHalfMiddleIndex]];
        }
        break;
      case "the smallest":
        result = firstHalf;
        break;
      case "the biggest":
        result = secondHalf;
        break;

    }
    return result;
  }
  
  console.log(ofThe([2, 9, 8, 5, 6, 3, 4, 7, 1], "the biggest")); // [9, 8, 7, 6, 5]
  