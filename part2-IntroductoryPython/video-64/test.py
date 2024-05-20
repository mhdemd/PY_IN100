names_string = "John,      Jane    , Alice, Bob, Mary"

# ["John", "Jane", "Alice", ...]

names = []
currrent_name = ""

for char in names_string:
    if char != ",":
        currrent_name += char
    else:
        names.append(currrent_name.strip())
        currrent_name = ""

names.append(currrent_name)
print(names)

# print(len("   Mehdi          "))

