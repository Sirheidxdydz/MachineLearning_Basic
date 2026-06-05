print("1. Enter some numbers ")
print("2. At the end of the input enter any symbol \n")

is_number = True
sum_value = 0

while is_number:

    user_input = input("Enter number: ")

    try:
        sum_value += float(user_input)

    except ValueError:
        #break
        is_number = False

print(f"\nSum of all numbers: {sum_value}")