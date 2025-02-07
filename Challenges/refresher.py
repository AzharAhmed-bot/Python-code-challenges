def atbashEncoder():
    alphabets='abcdefghijklmnopqrstuvwxyz'
    backwards=alphabets[::-1]
    result=dict()
    result.update(zip(alphabets,backwards))
    return result
    

print(atbashEncoder())

def atBash(string):
    alphabets='abcdefghijklmnopqrstuvwxyz'
    result=''
    for char in string:
        if char.isalpha():
            position=alphabets.index(char.lower())
            print(position)
            result+=alphabets[len(alphabets)-position-1] if char.islower() else alphabets[len(alphabets)-position-1].upper()
        else:
            result+=char
    
    return result

print(atBash('Ab cd'))
