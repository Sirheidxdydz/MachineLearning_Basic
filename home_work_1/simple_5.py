print('=' * 13 + "<Number sum>" + '=' * 13)
print("Enter 10 numbers\n")

max_number = 0

for _ in range(10):

    user_input = input("Enter number: ")
    number = float(user_input)

    if number > max_number:
        max_number = number

print(f"\nMax number: {max_number}")