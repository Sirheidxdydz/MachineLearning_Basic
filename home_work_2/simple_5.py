input_data = input("Enter some row: ").replace(" ", "").upper()

vowels = "АОУЫЭЕЁИЮЯAEYUIO"
consonant = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩCDFGHJKLMNPQRSTVWXYZ"
digits = "0123456789"

result_dict = {"гласные": 0, "согласные": 0, "цифры": 0, "пунктуация": 0}

for symbol in input_data:
    if symbol in vowels:
        result_dict["гласные"] += 1
    elif symbol in consonant:
        result_dict["согласные"] += 1
    elif symbol in digits:
        result_dict["цифры"] += 1
    else:
        result_dict["пунктуация"] += 1

print(result_dict)