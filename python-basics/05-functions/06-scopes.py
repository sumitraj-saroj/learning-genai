def serve_chai():
    chai_type = "masala chai"
    print(f"this is local scope : {chai_type}")  # Local scope


chai_type = "lemon"
serve_chai()

print(chai_type)


def chai_counter():
    chai_order = "Lemon"  # Enclosing scope

    def print_order():
        chai_order = "Ginger"
        print(f"Inner {chai_order}")

    print(f"outter {chai_order}")
    print_order()


chai_counter()

chai_order = "Tulsi"
print(f"Golbal hai {chai_order}")
