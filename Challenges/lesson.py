# P Y T H O N
first_name="Adrain"

integer=5

float=588.687686

boolean=False

character='k'
mass=4
acc=2

force=4 * 2


def power_of_number(base,exponent):
    answer=base ** exponent
    return answer


def quadratic_equation_solver(a,b,c=-2):
    x1=-b + (((b**2)+(4*a*c))**1/2)/(2*a)
    x2=-b + (((b**2)-(4*a*c))**1/2)/(2*a)
    return x1,x2


eq_1=quadratic_equation_solver(4,4,-2)
eq_2=quadratic_equation_solver(4,4)
eq_3=quadratic_equation_solver(4,4,5)
print("Equation 1: " ,eq_1)
print("Equation 2: " ,eq_2)
print("Equation 3: " ,eq_3)

sub=lambda a,b : a-b
# 1 +((number-1) %9)


def subtraction(a,b):
    diff=a-b
    return diff

subtraction(50,25)


# 345
# 3+4+5= 12
# 222
#2+2+2=6

def sum_of_number(number):
    answer=1 +((number-1) %9)
    return answer

sum=lambda number : 1+((number-1) %9)



print(sum_of_number(345))


# Check if a number is a prime number 
