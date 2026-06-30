def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elachi Chai"


stall = serve_chai()

for cup in stall:
    print(cup)


def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]


# Generator function


def get_chai_gem():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai = get_chai_gem()
print(next(chai))

print(next(chai))

print(next(chai))
# print(next(chai)) --> This will give error
#  for n in chai:
#     print(n)
