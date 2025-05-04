
def helper(n):
    if n == 0:
        return ""
    
    q= n // -2
    r = n % -2
    if r < 0:
        r+=2
        q+=1
    
    return helper(q) + str(r)

def negative_binary(i):
    if i == 0:
        return "0"
    
    return helper(i)

def binary_to_negative(s):
    result = 0
    for i, char in enumerate(reversed(s)):
        print(char + "*" + "-2" + "**" + str(i))
        result += int(char) * ((-2) ** i)
    return result




print(negative_binary(6))
print(binary_to_negative("11010"))