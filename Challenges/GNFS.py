import random


def gcd(a,b):
    a=abs(a)
    if b==0:
        return a
    return gcd(b, a%b)
    


def GNFS(num):
    while True:
        guess=random.randint(2,num-1)
        if num % guess !=0:
            break

    print(guess)
    r=1
    new_guess=pow(guess,r,num)

    max_iterations=1000
    while new_guess % num != 1 and r<max_iterations:
        r+=1
        new_guess=pow(guess,r)

    if r>=max_iterations:
        return f"Failed to find solution of r"

    first_multiple=0
    if r % 2 == 0:
        a=pow(guess,r/2)+1
        first_multiple+=gcd(a,num)

    second_multiple = num / first_multiple
    return (f"The prime number {num} has the multiples {first_multiple} * {second_multiple}")
    

        


print(GNFS(103))