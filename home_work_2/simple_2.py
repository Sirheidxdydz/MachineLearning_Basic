input_text = input("Input some row: ").strip()

marks = ".,:;!?"
input_row = input_text

for mark in marks:
    input_row = input_row.replace(mark, "")

word_list = input_row.split()

print(" ".join(word_list[::-1]))