# Filter values from a list

# filter (function, iterable)

my_list = [10,11,12,13,14,15]

print(list(filter(lambda x: x%2 == 0, my_list)))