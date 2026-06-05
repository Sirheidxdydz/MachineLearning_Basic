lists = [
    [2, 4, 5, 5, 2],
    ["cos(x)", 100, 56.6, "Sergio"],
    [90, "Anna", 4, "cos(x)"],
    ["Anna", "Nina", 2, 56.6, 1]
]

new_list = []
for item in lists:
    new_list.extend(item)

print(list(set(new_list)))

