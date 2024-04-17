start_num = int(input("Enter the start of the range: "))
end_num = int(input("Enter the end of the range: "))

for i in range(start_num, end_num + 1):
    for j in range(2, i):
        if i % j == 0:
            print(i, "is not a prime number")
            break
    else:  # If the inner loop completes successfully
        print(i, "is a prime number")
