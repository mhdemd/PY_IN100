class Car:
    # class attr
    attr1 = "Hello"

    # instance attr
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    #class def
    def print_hi():
        print("Hi")

    # instance def
    def print_id(self):
        print(id(self))

bmw = Car("BMW", "X6")
# print(id(bmw))

bmw.print_id()
bmw.__class__.print_hi()
