# # map
# def fun(n):
#     return n * 2

# my_list = [1, 2, 3, 4, 5]

# # result = map(fun, my_list)
# # print(list(result))

# result = map(lambda x : x * 2, my_list)
# print(list(result))

# ========================================
# Filter
def fun1(x):
    if x > 0:
        return True
    else:
        return False
    
def fun2(x):
    if x % 2 == 0:
        return True
    else:
        return False


my_list1 = [-1, 0, 1, 2, 3, 4]

# filtered_item = filter(fun1, my_list1)
# print(list(filtered_item))

# filtered_item = filter(fun2, my_list1)
# print(list(filtered_item))

# filtered_item = filter(lambda x : x > 0, my_list1)
# print(list(filtered_item))

filtered_item = filter(lambda x : x % 2 == 0, my_list1)
print(list(filtered_item))