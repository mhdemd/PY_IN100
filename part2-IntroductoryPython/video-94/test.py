# file = open(r"C:\Users\me6\Desktop\video-94\01.txt", "a")

## Read file
# for line in file:
#     print(line)
# print(file.read(20))
# print(file.readline(25))
# print(file.readlines(25))
# file.close()

## Write & append
# file = open(r"C:\Users\me6\Desktop\video-94\01.txt", "a")
# file.write("Hiiiiiiiiii222222!!!!!!!")
# file.close()

# file = open(r"C:\Users\me6\Desktop\video-94\01.txt", "a")
# try:
#     file.write("Hiiiiiiiiii222222!!!!!!!")
# finally:
#     file.close()

with open(r"C:\Users\me6\Desktop\video-94\01.txt", "w") as file:
    file.write("Use with \n")
    file.write("I am Mehdi Emadi \n")
    file.write("Welcome to my channel")


with open(r"C:\Users\me6\Desktop\video-94\01.txt", "r") as file:
    print(file.read())