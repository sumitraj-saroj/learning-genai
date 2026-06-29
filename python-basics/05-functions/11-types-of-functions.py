def pure_chai(cups):  # pure function
    return cups * 10


total_chai = 0


# Not recomemded
def impure_chai(cups):  # impure function
    global total_chai
    total_chai += cups


def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)


print(pour_chai(4))

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))


print(strong_chai)
print(chai_types)
