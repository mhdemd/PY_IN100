class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hi_person(self):
        print(f"Hi, {self.first_name} {self.last_name}!")
        
# person_1 = Person("Mehdi", "Emadi")
# person_1.hi_person()

class Iranian(Person):
    def __init__(self, first_name, last_name, id_number):
        self.id_number = id_number

        # invoking the __init__ of parent class
        Person.__init__(self, first_name, last_name)

    def detail_person(self):
        print(f"You are {self.first_name} {self.last_name} "
              f"with id number: {self.id_number}"
              )
        
person_2 = Iranian("Mehdi", "Emadi", "002001001002")
# attrs:
print(person_2.first_name)
print(person_2.id_number)

# methods:
person_2.hi_person()
person_2.detail_person()
