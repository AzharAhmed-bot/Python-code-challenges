
def rot13(message):
    result=""
    for char in message:
        if char.isalpha():
             charNumber=ord('a') if  char.islower() else ord('A')
             result += chr((ord(char) - charNumber + 13) % 26 + charNumber)
        else:
            result+=char
        
    return result
print(rot13("Hello World"))