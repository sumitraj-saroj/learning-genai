chai_type = "Plain Chai"


def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irani"

    kitchen()


front_desk()

print(f"The value is : {chai_type}")
