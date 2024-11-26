# a = 2 
# print(a == 1)

try:
    a = 1
    b = 1 / 0

except NameError:
    print("NameError!!!")

except ZeroDivisionError:
    print("ZeroDivisionError!!!")   

else:
    print("ok!!!")

finally:
    print("Done!")
