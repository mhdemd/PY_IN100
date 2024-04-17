start_num = int(input("Enter the start of the range: "))
end_unm = int(input("Enter the end of the range: "))

for i in range(start_num, end_unm + 1):
    for j in range(2, i):
        if i % j == 0:
            print(i, "is not a prime number!") 
            break   
    else:
        print(i, "is a prime number")
