input_text = input("Enter some string:")

letters = sorted(set(input_text))
dict_data = {x: input_text.count(x) for x in letters}

print(dict_data)