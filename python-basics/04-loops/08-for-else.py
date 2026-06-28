staff = [("sumit", 23), ("Zara", 25)]

for name, age in staff:
    if age > 30:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No is eligible to manage the staff")
