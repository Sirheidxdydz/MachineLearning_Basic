print('=' * 13 + '<Upper register row>' + '=' * 13 + '\n')

user_input = input("Enter some row: ")
upper_row = ''

for symbol in user_input:

    if symbol.isalpha() and symbol == symbol.upper():
        upper_row += symbol

print(f"Upper_case row: {upper_row}")


