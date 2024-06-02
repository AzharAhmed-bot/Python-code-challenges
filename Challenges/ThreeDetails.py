
# This problem can be solved using dynamic programming.
# Dynamic Programming is a method used in mathematics and computer science to solve complex problems by breaking them down into simpler subproblems. 
# By solving each subproblem only once and storing the results, it avoids redundant computations, leading to more efficient solutions for a wide range of problems.

def three_details(n):
    if n % 2 == 0:
        return 2 ** (n // 2)
    else:
        return 1

print(three_details(6))