# Types of Python Function Arguments

# Positional arguments
# def person(first_name, last_name):
#     print(f"You are {first_name} {last_name}.")
# person("Emadi", "Mehdi")

# Keyword arguments
# def person(first_name, last_name):
#     print(f"You are {first_name} {last_name}.")
# person(last_name = "Emadi", first_name = "Mehdi")
# person(first_name = "Mehdi", last_name = "Emadi")

# Default arguments
# def person(first_name, last_name = "Emadi"):
#     print(f"You are {first_name} {last_name}.")
# person(first_name= "Mehdi", last_name= "Karimi")
# person()

# Arbitrary arguments
# *args
# def person(*args):  # as Tuple
#     print(args)
#     print(args[0], args[3])
# person("Mehdi", "Emadi", "Python", "100", "s")

def person(f_name, l_name, *args):  # as Tuple
    if args:
        print(f_name, l_name, args[0])
    else:
        print(f_name, l_name)
        
person("Mehdi", "Emadi", "Python", "100", "s")
person("Mehdi", "Emadi")

# **kwargs