# Create a list based on existing lists

words = ['Austria','Brazil','Bulgaria']

capitalized = []
for word in words:
    capitalized.append(word.title())

print(capitalized)

# better way to write it
# [expression for item in list]

capitalized = [word.title() for word in words]

print(capitalized)
