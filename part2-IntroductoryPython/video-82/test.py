import random
import string
import time

# تابعی برای تولید رشته‌های تصادفی
def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# ایجاد دیکشنری با ۱۰۰۰ عضو
dict_example = {generate_random_string(): random.randint(1, 100) for _ in range(1000)}

# ایجاد لیست تودرتو بر اساس دیکشنری
list_example = [[key, value] for key, value in dict_example.items()]

# ==============================================================================
# دکوریتور برای اندازه‌گیری زمان اجرا
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.20f} seconds")
        return result
    return wrapper

# تابع برای دسترسی به آیتم دیکشنری
@measure_time
def access_dict_item_multiple_times(dictionary, key, iterations):
    for _ in range(iterations):
        _ = dictionary.get(key)

# تابع برای دسترسی به آیتم لیست تودرتو
@measure_time
def access_list_item_multiple_times(nested_list, key, iterations):
    for _ in range(iterations):
        _ = next((value for k, value in nested_list if k == key), None)

# ==============================================================================
# انتخاب یک کلید تصادفی برای دسترسی
random_key = list(dict_example.keys())[-1]

# تعداد تکرارها
iterations = 10000

# دسترسی به آیتم دیکشنری چندین بار
access_dict_item_multiple_times(dict_example, random_key, iterations)

# دسترسی به آیتم لیست تودرتو چندین بار
access_list_item_multiple_times(list_example, random_key, iterations)
