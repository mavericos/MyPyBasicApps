# Sort dictionary by values

# sorted(iterable, key=None, reverse=False)

population = {'USA': 329.5, 'Bulgaria': 7.1, 'UK': 70.5}
print(sorted(population.items(), key=lambda x:x[1]))

# better way

my_dict = {k: v for k, v in sorted(population.items(), key=lambda x: x[1])}
print(my_dict)
