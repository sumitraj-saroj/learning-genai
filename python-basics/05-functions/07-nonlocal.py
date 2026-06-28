def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"

    kitchen()
    print(f"After kicten update what's the value : {chai_type}")


update_order()
