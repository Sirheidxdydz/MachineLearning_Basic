print('=' * 13 + '<Sum of digits>' + '=' * 13)

user_input = input("Enter some row: ")

digit_sum = 0

for symbol in user_input:

    if symbol in "0123456789":
        digit_sum += int(symbol)

print(f"\nSum of all digits: {digit_sum}")