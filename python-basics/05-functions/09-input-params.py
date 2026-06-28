chai = "Ginger Chai"


def prepare_order(order):
    print("Preparing", order)


prepare_order(chai)


def make_order(tea, milk, sugar):
    print(tea, milk, sugar)


make_order("Darjeeling", "Yes", "low")  # postional
make_order(tea="Mumbai", milk="No", sugar="Yes")  # keywords


def special_tea(*ingredients, **extras):
    print("ingredients", ingredients)
    print("extras", extras)


special_tea("Cinnamon", "Giner", sweetner="honey", foam="yes")

#
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)
#


def chai_order(order=None):
    if order is None:
        order = []
    print(order)


chai_order()
chai_order()
