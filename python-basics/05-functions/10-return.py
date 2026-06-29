def make_chai():
    return "Here is your chai"


# Nothing --> implicitly returns **NONE**
#
#
# One Value
# Multiple Value
# early value from a function


print(make_chai())


def ideal_chaiwala():
    pass


print((ideal_chaiwala()))


def sold_cups():
    return 120


print(sold_cups())


def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, Chai is over"
    return "Chai is ready"


print(chai_status(0))
print(chai_status(7))


def chai_report():
    return 100, 208, 676


sold, remaining, _ = chai_report()

print(sold)
print(remaining)
