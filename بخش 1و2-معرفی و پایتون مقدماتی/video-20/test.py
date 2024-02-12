a, b, c = 15, 15, 10

print(a,b,c)
print(a // 3) # خارج قسمت
print(a % 3) # باقیمانده

if c % 3 == 0:
    print("Ok")
else:
    print("Not Ok")

print("Ok") if c % 3 == 0 else print("Not Ok")
