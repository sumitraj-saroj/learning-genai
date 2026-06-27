ingredients = ["water", "milk", "tea leaves"]

ingredients.append("sugar")
print(f"ingredients are: {ingredients}")

ingredients.remove("water")

print(f"ingredients are: {ingredients}")

chai_option = ["black tea", "olong tea", "red tea"]
more_chai = ["green tea", "simple tea"]

chai_option.extend(more_chai)

print(f"Total chai : {chai_option}")

chai_option.insert(2, "masala chai")

print(f"Total chai : {chai_option}")
chai_option.pop()

chai_option.reverse()
print(f"Total chai : {chai_option}")

chai_option.sort()

print(f"Total chai : {chai_option}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]
full_liquid_mix = base_liquid + extra_flavor

print(f"Total liquid : {full_liquid_mix}")

raw_spices_data = bytearray(b"CINNAMON")


print(f"bytearray: {raw_spices_data}")

raw_new_spice = raw_spices_data.replace(b"CINN", b"CARD")

print(f"byte: {raw_new_spice}")
