def rgb(r, g, b):
    result = []
    
    # Check and handle the red component
    if r > 255:
        result.append("FF")
    elif r <= 0:
        result.append("00")
    else:
        result.append(format(r, '02X'))
    
    # Check and handle the green component
    if g > 255:
        result.append("FF")
    elif g <= 0:
        result.append("00")
    else:
        result.append(format(g, '02X'))
    
    # Check and handle the blue component
    if b > 255:
        result.append("FF")
    elif b <= 0:
        result.append("00")
    else:
        result.append(format(b, '02X'))
    
    # Concatenate the result list to form the hexadecimal representation of the RGB color
    return "".join(result)

print(rgb(-20, 275, 125)) 