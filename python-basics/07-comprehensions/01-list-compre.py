menu = ["masala Chai", "Iced lemon chai", "Green tea", "Iced peach tea", "Ginger tea"]

iced_tea = [tea for tea in menu if "Iced" in tea]


# iced_tea = [tea for tea in menu if len(tea) < 12]
print(iced_tea)
