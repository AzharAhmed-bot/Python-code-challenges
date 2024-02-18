
def rot13(message):

    result=""
    # Iterate through the messages
    for char in message:
        # Check if the character is alphanumerical ie numbers, letters and special symbols so that we keep white spaces and 
        if char.isalpha():
            #  Ord converts char to ASCII
            #  Get the character ASCII. In this case it is 97 for a and 65 for A
             charNumber=ord('a') if  char.islower() else ord('A')
            #  chr converts Ascii to char 
            #  Consider a letter H and its ascii is 72 
            #  (72-65+13) %(modulas) 26= 20 + 65= 85 converted to char its U
             result += chr((ord(char) - charNumber + 13) % 26 + charNumber)
        else:
            result+=char
        
    return result
print(rot13("Hello World"))