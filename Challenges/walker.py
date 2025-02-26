import math

def walker(a, b, c, alpha, beta, gamma):
    angle_ABh = 180 - (90 + beta)
    angle_ABC = 180 - (angle_ABh + gamma)

    line_AC_sq = (b**2) + (c**2) - (2 * b * c * math.cos(math.radians(angle_ABC)))
    line_AC = math.sqrt(line_AC_sq)  

    line_OC = math.sqrt(line_AC_sq - (a**2))

    cos_AOC = ((a**2) + (line_OC**2) - (line_AC_sq)) / (2 * a * line_OC)

    cos_AOC = max(-1, min(1, cos_AOC))

    angle_AOC = math.degrees(math.acos(cos_AOC))  

    angle_tOC=alpha+round(angle_AOC)
    print(angle_tOC)

    return round(line_OC),angle_tOC

# Test the function
print(walker(12, 20, 18, 45, 30, 60))
