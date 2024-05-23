# First class functions => Decorators

# as variable
# def fun1(x):
#     print(x)
# fun1("Hello")

# fun2 = fun1
# fun2("Hi")

# pass to fun
# def fun1(fun):
#     fun("Hello")

# def fun2(x):
#     print(x)

# fun1(fun2)

# return fun
# def main(x):
#     def add(y):
#         return x + y
#     # add = "Hello"

#     return add

# first = main(3)
# print(first)

# second = main(3)(2)
# print(second)


# Store in data structures
def fun(x):
    return x + 1

a = [1, 3.14, "Hello", fun]
var = a[3](4)
print(var)
