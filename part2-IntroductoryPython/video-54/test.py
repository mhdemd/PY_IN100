phone_book = {
    "+9891200000000" : "Susan",
    "+9891200000001" : "Saman",
    "+9891200000002" : "Sara",
}

# print(phone_book.items())

# for phone_number, name in phone_book.items():
#     print(f"Happy New Year, {name}!")

for phone_number in phone_book:
    if phone_number == "+9891200000001":
        print(phone_book[phone_number])
