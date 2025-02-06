
# The best solution to this problem is I think using recursion to convert integers to words
# So we use the simple mathematics of place value:
# Give the number 345
# 5- ones
# 4- tens
# 3- hundreds
# But we also have to account for negative numbers and teen numbers
def wordify(n):
    ones=["zero","one","two","three","four","five","six","seven","eight","nine"]
    teens=["ten","eleven", "twelve","thirteen","forteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    def rec(num):
        if num<10:
            return ones[num]
        elif num < 20:
            return teens[num-10]
        elif num < 100:
            return tens[num // 10] + (" "+rec(num % 10) if num%10!=0 else "")
        elif num < 1000:
            return rec(num//100) + " hundred" + (" "+rec(num%100) if num%100!=0 else "")
        
    result=rec(n)
    return result

print(wordify(223))