def mirror(list):
    sort=sorted(list)
    print(sort)
    return sort[:-1]+sort[::-1]

print(mirror([-3, 15, 8, -1, 7, -1]))