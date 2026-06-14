def integer_input():

    while True:
        num = input("Enter integer number: ")
        try:
            num = int(num)
            print("Accepted!")
            break
        except ValueError:
            print("Not integer! Try again!")

integer_input()
