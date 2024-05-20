names_string = "John,  Jane,   Alice, Bob   , Mary"

# ["John", "  Jane", "  Alice", ...]

result = names_string.split(",")
# print("result is: ", result)

# new_result = []
# for name in result:
#     new_result.append(name.strip())
# print("new_result is: ", new_result)

# List Comprehension
# A = [1, 2, 3, 4, 5, 6]
# A2 = [x*2 for x in A]

# print(A)
# print(A2)

new_result = [name.strip() for name in result]
print(result)
print(new_result)
