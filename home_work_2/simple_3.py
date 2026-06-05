object_list = [99, 3, 99, "Anna", 4, 2, 2, 5, 6, 4, 3, "Lina", "Anna"]

s = set()
distinct_list = [i for i in object_list if not (i in s or s.add(i))]

print(distinct_list)