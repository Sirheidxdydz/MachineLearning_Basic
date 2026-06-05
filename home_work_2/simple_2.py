input_text = input("Input some row: ").strip()

marks = ".,:;!?"

for mark in marks:
    input_row = input_text.replace(mark, "")

word_list = input_text.split()

print(" ".join(word_list[::-1]))