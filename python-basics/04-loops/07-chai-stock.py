flavours = ["Ginger", "Out of stock", "Lemon", "Discontiuned", "Tulsi"]


for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontiuned":
        break
    print("Discontiuned item found")
print("Outside of loops")
