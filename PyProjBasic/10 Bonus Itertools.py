# Bonus - Itertools

import itertools

first = [1, 2, 3, 4, 5]
sum_list = itertools.accumulate(first)
print(list(sum_list))

first2 = ['A', 'B', 'C', 'D']
chain_list = itertools.chain(first, first2)
print(list(chain_list))

names = ['Tim', 'Joe', 'Bill', 'Susan', 'Jen']
show = [1, 0, 1, 1, 0]  # Извежда само names, които съвпадат с 1
compressed_list = itertools.compress(names, show)
print(list(compressed_list))

