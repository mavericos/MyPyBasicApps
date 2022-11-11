# Comprehensions

x = [i for i in range (100) if i % 2 == 0]

print(x)


y = [a*b for a in range (13) for b in range(10)]

print(y)

z = [[0 for _ in range(5)] for _ in range (5)]

print(z)

h = (i for i in "zdrasti")
print(tuple(h))

sentence = "Hi there, who are you"
g = {char: sentence.count(char) for char in set(sentence)}
print(g)

