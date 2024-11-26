class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    

# class Iranian(Person):
#     def __init__(self, first_name, last_name, id_number):
#         self.id_number = id_number

#         # invoking the __init__ of parent class
#         # Person.__init__(self, first_name, last_name)
#         super().__init__()

class Iranian(Person):
    def __init__(self, first_name, last_name, id_number):
        super().__init__(first_name, last_name)
        self.id_number = id_number
'''
مزایای استفاده از super:

کاهش وابستگی به نام کلاس والد
پشتیبانی بهتر از چند وراثت
خوانایی و نگهداری بهتر
'''
person_2 = Iranian("Mehdi", "Emadi", "002001001002")
# attrs:
print(person_2.first_name)
print(person_2.last_name)
print(person_2.id_number)
