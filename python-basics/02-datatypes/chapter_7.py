masala_spices = ("Ginger", "cloves", "cinnamon")
(spiec1, spice2, spice3) = masala_spices
print(f"This are my spieces: {spiec1}, {spice2}, {spice3}")

ginger_ratio, cinnamon_ratio = (2, 1)

print(f"This Ratio is G : {ginger_ratio} and C: {cinnamon_ratio}")

ginger_ratio, cinnamon_ratio = cinnamon_ratio, ginger_ratio

print(ginger_ratio, cinnamon_ratio)

# Membership

print(f"Is Ginger in Masala Spices ? {'Ginger' in masala_spices}")  # Case Sensitive
