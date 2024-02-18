import re
import itertools

def latest_clock(a, b, c, d):
    # Define a regular expression pattern to validate time format
    time_pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
    
    # Create a list of the input digits
    myArr = [a, b, c, d]
    
    # Initialize an empty list to store valid time permutations
    result = []
    
    # Generate permutations of the input digits
    permutation = itertools.permutations(myArr)
    
    # Iterate through each permutation
    for perm in permutation:
        # Concatenate the first two digits as hours and the last two as minutes
        time = ''.join(map(str, perm[:2])) + ":" + ''.join(map(str, perm[2:]))
        
        # Check if the generated time matches the specified format
        if re.match(time_pattern, time):
            # If the time is valid, append it to the result list
            result.append(time)
    
    # Find the latest valid time among the generated permutations
    max_time = max(result)
    
    # Return the latest valid time
    return max_time

print(latest_clock(1,9,8,3))