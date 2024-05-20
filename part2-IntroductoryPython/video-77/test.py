# def fun1(x):
#     x += 1

#     def fun2(y):
#         y += 1
#         return y
    
#     return fun2(x)

# print(fun1(20))

def fun(list):
    def odd_even(list):
        odd = []
        even = []
        for item in list:
            if item % 2 == 0:
                odd.append(item)
            else:
                even.append(item)
        print(f"My Odd List: {odd}\n"
              f"My Even List: {even}")

    return odd_even(list)

fun([1,2,3,4,5])
