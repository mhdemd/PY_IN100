# def fun(x:str) -> int:  # x ==> parameter
#     x += 1
#     return x

# print(fun(30.6))  # 30 ==> arguments
    
# for i in range(5):
#     pass

# print_hi()

# x = 10
# if x > 5:
#     pass

# print_hi()

# for j in range(7):
#     pass

# print_hi()

def fun(num):
    if num > 10:
        print("Your number is greater than 10")
    else:
        print("Not")

    for i in range(5):  # 0, 1, 2, 3, 4
        num += 1
    return num

x = fun(16)  # 16+5
print(x)



