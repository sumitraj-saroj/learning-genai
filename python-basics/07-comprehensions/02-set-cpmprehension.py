flavorite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Chai",
    "Green Tea",
    "Elachi Tea",
]

unique_tea = {chai for chai in flavorite_chais}
print(unique_tea)

recipes = {
    "Masala Chai": ["Ginger", "cademon", "cloves"],
    "Elachi Chai": ["cademon", "milk"],
    "Spicey Chai": ["Ginger", "Black peper", "cloves"],
}
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)
