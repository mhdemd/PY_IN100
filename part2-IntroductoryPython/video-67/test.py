names_string = "John, Jane, Alice, Bob, Mary"

## First method
# new_string = ""
# for char in names_string:
#     if char != ",":
#         new_string += char
#     else:
#         new_string += "??"
# print(new_string)

## Second method
# new_string = ""
# for char in names_string:
#     new_string += char if char != "," else "??"
# print(new_string)

## Third method
# names_list = [char if char != "," else "??" for char in names_string]
# new_string = "".join(names_list)
# print(new_string)

## Fourth method
new_string = names_string.replace(",", "???ejh")
print(new_string)
