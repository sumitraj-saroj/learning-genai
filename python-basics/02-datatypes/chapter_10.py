chai_order = dict(type="Masala Tea", size="Large", sugar=2)


print(f"Chai Order:{chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"

chai_recipe["liquid"] = "milk"

print(f"Chai Recipe: {chai_recipe}")

del chai_recipe["liquid"]
