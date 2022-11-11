# Sort dictionary by keys

# {key: value for key, value in iterable}

product_prices = {'Z':9.99, 'Y':9.99, 'X':9.99}
product_prices_sorted = {key: product_prices[key] for key in sorted(product_prices.keys())}
print(product_prices_sorted)