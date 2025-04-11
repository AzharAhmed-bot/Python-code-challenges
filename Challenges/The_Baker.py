def cakes(recipe,available):
    return min(available.get(ingredient, 0) // amount for ingredient, amount in recipe.items())


def new_cakes(recipe,available):
    result=[]
    for ingredient, amount in recipe.items():
        result.append(available.get(ingredient,0) // amount)
    return min(result)


recipe={'flour': 500, 'sugar': 200, 'eggs': 1}
available={'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}

print(cakes(recipe, available))
print(new_cakes(recipe, available))
