def chai_flavour(flavour="Masala"):
    """Returns the flavour of chai"""
    return flavour


print(chai_flavour.__doc__)

print(chai_flavour.__name__)

# help(len)


def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa
    :param chai: Number of chai cups (10 rupees)
    :params samosa: Number of samosa (15 rupees)
    :return: total amount and thank you
    """
    total = chai * 10 + samosa * 15
    return total


print(generate_bill(12, 32))
