def palindrom(num):
    if isinstance(num,str)  or num < 0 :
        return "Not valid"
    number_string=str(num)    
    n=len(number_string)
    result=[]
    for i in range(n):
        for j in range(i+1,n+1):
            substring=number_string[i:j]
            if len(substring) > 1 and substring==substring[::-1]:
                if not substring.startswith('0'):
                    print(substring)
                    result.append(int(substring))

    for num in result:
        if num<10:
            result.remove(num)
        
    return "No palindromes found" if len(result) == 0 else sorted(list(set(result)))
                
    



print(palindrom(59332800303))

    


    