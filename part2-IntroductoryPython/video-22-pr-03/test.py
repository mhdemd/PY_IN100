# درخواست ورود اطلاعات از کاربر
gender = str(input("Enter your gender (Male or Female): ")) # "جنسیت خود را وارد کنید (آقا یا خانم): "

# اضافه کردن شرط برای بررسی جنسیت صحیح
if gender == "Male" or gender == "Female":
    age = int(input("Enter your age: ")) # "سن خود را وارد کنید: "
    weight = float(input("Enter your weight in kilograms: ")) # "وزن خود را به کیلوگرم وارد کنید: "

    # محاسبه مقدار کالری مورد نیاز بر اساس جدول
    calories_needed = 0

    if gender == "Female": # "خانم"
        if age >= 18 and age <= 35:
            if weight >= 45 and weight <= 50:
                calories_needed = 1760
            elif weight > 50 and weight <= 55:
                calories_needed = 1860
            elif weight > 55 and weight <= 60:
                calories_needed = 1950
            elif weight > 60 and weight <= 65:
                calories_needed = 2050
            elif weight > 65 and weight <= 70:
                calories_needed = 2150
            elif weight > 70 and weight <= 75:
                calories_needed = 2250
            elif weight > 75:
                calories_needed = 2400
        elif age >= 36 and age <= 55:
            if weight >= 45 and weight <= 50:
                calories_needed = 1570
            elif weight > 50 and weight <= 55:
                calories_needed = 1660
            elif weight > 55 and weight <= 60:
                calories_needed = 1760
            elif weight > 60 and weight <= 65:
                calories_needed = 1860
            elif weight > 65 and weight <= 70:
                calories_needed = 1960
            elif weight > 70 and weight <= 75:
                calories_needed = 2050
            elif weight > 75:
                calories_needed = 2150
        elif age > 55:
            if weight >= 45 and weight <= 50:
                calories_needed = 1430
            elif weight > 50 and weight <= 55:
                calories_needed = 1500
            elif weight > 55 and weight <= 60:
                calories_needed = 1550
            elif weight > 60 and weight <= 65:
                calories_needed = 1600
            elif weight > 65 and weight <= 70:
                calories_needed = 1630
            elif weight > 70 and weight <= 75:
                calories_needed = 1660
            elif weight > 75:
                calories_needed = 1720
    elif gender == "Male": # "آقا"
        if age >= 18 and age <= 35:
            if weight >= 40 and weight <= 45:
                calories_needed = 1400
            elif weight > 45 and weight <= 50:
                calories_needed = 1500
            elif weight > 50 and weight <= 55:
                calories_needed = 1600
            elif weight > 55 and weight <= 60:
                calories_needed = 1700
            elif weight > 60 and weight <= 65:
                calories_needed = 1800
            elif weight > 65 and weight <= 70:
                calories_needed = 1900
            elif weight > 70:
                calories_needed = 2000
        elif age >= 36 and age <= 55:
            if weight >= 40 and weight <= 45:
                calories_needed = 1300
            elif weight > 45 and weight <= 50:
                calories_needed = 1400
            elif weight > 50 and weight <= 55:
                calories_needed = 1500
            elif weight > 55 and weight <= 60:
                calories_needed = 1600
            elif weight > 60 and weight <= 65:
                calories_needed = 1700
            elif weight > 65 and weight <= 70:
                calories_needed = 1800
            elif weight > 70:
                calories_needed = 1900
        elif age > 55:
            if weight >= 40 and weight <= 45:
                calories_needed = 1200
            elif weight > 45 and weight <= 50:
                calories_needed = 1300
            elif weight > 50 and weight <= 55:
                calories_needed = 1400
            elif weight > 55 and weight <= 60:
                calories_needed = 1500
            elif weight > 60 and weight <= 65:
                calories_needed = 1600
            elif weight > 65 and weight <= 70:
                calories_needed = 1700
            elif weight > 70:
                calories_needed = 1800

    # نمایش مقدار کالری مورد نیاز به کاربر
    print(f"Your daily calorie requirement: {calories_needed}") # مقدار کالری مورد نیاز روزانه شما:
else:
    print("Enter correct gender!") # جنسیت صحیح وارد کنید
