#  I want to wordify an integer
# Possible solutions?
# 1. Store the numbers in an array in word form(wont work)
# 2. Crazy if statements (would work but inefficient)
# 3. Place value? (haaa yesss!!!!)
# Lets say we have a number 301
# 3- place value is hundred
# 0-place value is tens
# 1- place value is
def wordify(n):
    single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]
    def helper(num):
        if num < 10:
            return single_digits[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + " " +(helper(num%10) if num%10!=0 else "")
        elif num < 1000:
            return single_digits[num // 100] + " hundred " + (helper(num%100) if num%100!=0 else "")
    
    result=helper(n)

    return result
            
        
        


print(wordify(351))
            