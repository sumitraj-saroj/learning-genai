essential_spices = {"cardamon", "ginger", "cinnamon"}

optional_spice = {"cloves", "ginger", "black peper"}

all_spices = essential_spices | optional_spice

print(f"All spices are:{all_spices}")

common_spices = essential_spices & optional_spice

print(f"Common Spices:{common_spices}")

only_in_essential = essential_spices - optional_spice

print(f"Only in essential :{only_in_essential}")
