# Luhn's algorithm
# Its basically invented in 1960 to verify id numbers most used is credit cards

# Given a series of numbers
# Double the digits at the even positions preferably from the right
# If we have one of the double digits reversed am gonna add the 2 digits eg 16=1+6=7
# Add all of them together and find if its divisible by 10

def luhns(number):
    result=[]
    total=0
    for i,num in zip(range(len(number)),number):
        if i%2!=0 and i!=0:
            result.append(int(num)*2)
        else:
            result.append(int(num))
    
    for num in result:
        if num>9:
            # Check 18//10=1 18%10=8 8+1=9
            result[result.index(num)]=num%10+num//10
    
    for num in result:
        total+=num
    
    return True if total%10==0 else False


def optimizedLuhns(number):
    total=0
    for i,num in enumerate(reversed(number)):
        integer=int(num)
        if i%2!=0:
            integer*=2
            if integer>9:
                integer=integer%10+integer//10
        total+=integer
    
    return True if total%10==0 else False
            


        

print(luhns('79927398713'))
print(optimizedLuhns('79927398713'))