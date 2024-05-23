# def fun(list):
#     def odd_even(list):
#         odd = []
#         even = []
#         for item in list:
#             if item % 2 == 0:
#                 odd.append(item)
#             else:
#                 even.append(item)
#         print(f"My Odd List: {odd}\n"
#               f"My Even List: {even}")

#     return odd_even(list)

# fun([1,2,3,4,5])

# ==============================================
# Lambda fun
# def fun(x):
#     x += 1
#     return x

# print(fun(20))

# lambda_fun = lambda x : x + 1
# print(lambda_fun(20))

# ==============================================
def filter_num(numbers_list, condition):
    filtered_list_1 = [] # زوج
    filtered_list_2 = [] # فرد
    for item in numbers_list:
        if condition(item):
            filtered_list_1.append(item)
        else:
            filtered_list_2.append(item)
    return filtered_list_1, filtered_list_2

# ============================================== odd & even
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_list_1, filtered_list_2 = filter_num(numbers, lambda x : x % 2 == 0)
print(f"list of even number: {filtered_list_1}")
print(f"list of odd number: {filtered_list_2}")

# ============================================== positive & negative
numbers = [1, 2, -3, -4, 5, -6, 7, 8]
filtered_list_1, filtered_list_2 = filter_num(numbers, lambda x : x > 0)
print(f"list of positive number: {filtered_list_1}")
print(f"list of negative number: {filtered_list_2}")

# ============================================== int & float


# ============================================== multiple 3 & Not multiple 3
