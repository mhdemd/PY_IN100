# Decorators
# def main(function):
#     function("Hi")

# @main
# def fun(string):
#     print(string)

# @main
# def fun1(string):
#     print(string + " Mehdi")

# main(fun)
# main(fun1)

# =============================================
def before_after(fun):
    def print_before_after():
        print("Before!")
        fun()
        print("After!")

    return print_before_after

# before_after()()

@before_after
def now():
    print("Now")
now()

# def now():
#     print("Now")
# before_after(now)()
