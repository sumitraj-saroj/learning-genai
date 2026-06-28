menu = ["Green", "Lemon", "Masala", "Red"]

for m in menu:
    print(f"Meni item is: {m}")


# enumerate

for index, item in enumerate(menu, start=1):
    print(f"Menu item is: {index} for {item}")
